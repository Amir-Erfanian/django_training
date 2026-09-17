from django.shortcuts import render
from .forms import ContactForm


def home(request):
    return render(request, 'core/home.html', {
        'name':'Amir',
        "skills": [
            "Python",
            "Django",
            "HTML",
            "CSS",
]
    })


def about(request):
    return render(request, 'core/about.html')




def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            print(name)
            print(email)
            print(message)

    else:
        form = ContactForm()

    return render(request, "core/contact.html", {
        "form": form,
    })