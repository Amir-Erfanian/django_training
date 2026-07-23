from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "email"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Full Name",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Age",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email",
                }
            ),
        }

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 5:
            raise forms.ValidationError("Age must be at least 5.")

        if age > 120:
            raise forms.ValidationError("Invalid age.")

        return age

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    LEVELS = [
        ("1", "Beginner"),
        ("2", "Intermediate"),
        ("3", "Advanced"),
    ]

    level = forms.ChoiceField(choices=LEVELS)
    level = forms.ChoiceField(choices=LEVELS, widget=forms.RadioSelect )
    languages = forms.MultipleChoiceField(

        choices=[
            ("py", "Python"),
            ("js", "JavaScript"),
            ("java", "Java"),
        ],
        widget=forms.CheckboxSelectMultiple

    )


class FeedbackForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Full Name",
            }
        )
    )

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if len(name.split()) < 2:
            raise forms.ValidationError(
                "Enter your full name."
            )

        return name

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    def clean_email(self):

        email = self.cleaned_data["email"]

        blocked = [
            "mailinator.com",
            "10minutemail.com",
            "tempmail.com",
        ]

        if email:

            domain = email.split("@")[1]

            if domain in blocked:
                raise forms.ValidationError(
                    "Temporary email addresses are not allowed."
                )

        return email

    rating = forms.ChoiceField(
        choices=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
        ],
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        )
    )

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your feedback...",
            }
        )
    )

    course = forms.ChoiceField(
        choices=[
            ("python", "Python"),
            ("django", "Django"),
            ("react", "React"),
            ("postgresql", "PostgreSQL"),
        ],
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        )
    )

    def clean_comment(self):

        comment = self.cleaned_data["comment"]

        if len(comment) < 20:

            raise forms.ValidationError(
                "Comment must contain at least 20 characters."
            )

        return comment