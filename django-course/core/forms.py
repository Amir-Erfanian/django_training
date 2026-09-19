from django import forms
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):

    name = forms.CharField(
        label="Your Name",
        max_length=100,
        error_messages={
    'required': 'Please enter your name.',
    },
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your name'
            }
        )
    )

    email = forms.EmailField(
        label="Email Address",
        error_messages={
    'required': 'Please enter your email address.',
    'invalid': 'Please enter a valid email address.',
    },
        widget=forms.EmailInput(
            attrs={
                'placeholder':"you@example.com"
            }
        )
    )

    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your message...',
                'rows': 5,
            }
        ),
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title.strip()) < 5:
            raise forms.ValidationError(
                'Title must be at least 5 characters long.'
            )

        return title

    def clean_content(self):
        content = self.cleaned_data['content']

        if len(content.strip()) < 20:
            raise forms.ValidationError(
                'Content must be at least 20 characters long.'
            )

        return content

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content:
            if title.strip().lower() == content.strip().lower():
                raise forms.ValidationError(
                    'Title and content should not be identical.'
                )

        return cleaned_data


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'location',
            'website',
            'profile_image',
        ]