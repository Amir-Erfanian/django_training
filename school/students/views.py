from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm, ContactForm, FeedbackForm
from .models import Student


def student_list(request):
    query = request.GET.get("q", "")

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query)
            | Q(email__icontains=query)
        )

    context = {
        "students": students,
        "query": query,
        "total_students": students.count(),
    }

    return render(
        request,
        "students/student_list.html",
        context,
    )


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(
        request,
        "students/student_detail.html",
        {
            "student": student,
        },
    )


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Student created successfully.",
            )
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "title": "Add Student",
        },
    )


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Student updated successfully.",
            )
            return redirect("student_detail", pk=student.pk)

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "title": "Edit Student",
        },
    )


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()

        messages.success(
            request,
            "Student deleted successfully.",
        )

        return redirect("student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {
            "student": student,
        },
    )


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                "Your message has been sent successfully."
            )
            form = ContactForm()

    else:
        form = ContactForm()

    return render(
        request,"students/contact.html",
        {
            "form": form,
        }
    )

def feadback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                "Your feadback is sent."
            )
            form = FeedbackForm()
    else:
        form = FeedbackForm()
    return render(request, "students/feadback.html",{
            "form": form
        })