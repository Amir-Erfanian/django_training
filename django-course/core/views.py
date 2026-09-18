from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, PostForm
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'core/home.html', {
        'name':'Amir',
        'posts' : posts,
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

def post_list(request):
    posts = Post.objects.all()

    return render(request, 'core/post_list.html', {
        'posts': posts,
    })

def post_create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('post_list')

    else:
        form = PostForm()

    return render(request, 'core/post_create.html', {
        'form': form,
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    return render(request, 'core/post_detail.html', {
        'post': post,
    })

def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

            return redirect('post_detail', id=post.id)

    else:
        form = PostForm(instance=post)

    return render(request, 'core/post_update.html', {
        'form': form,
        'post': post,
    })

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()

        return redirect('post_list')

    return render(request, 'core/post_delete.html', {
        'post': post,
    })