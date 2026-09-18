from django import forms
from .models import Post

class ContactForm(forms.Form):

    name = forms.CharField(
        label="Your Name",
        max_length=100,
    )

    email = forms.EmailField(
        label="Email Address",
    )

    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea,
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']