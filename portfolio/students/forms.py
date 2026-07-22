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
