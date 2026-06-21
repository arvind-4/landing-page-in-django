"""Forms for the landing app."""

from django import forms


class RegisterForm(forms.Form):
    """Form for email registration."""

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "label": "",
                "placeholder": "Email Address ...",
            },
        ),
    )
