from django import forms
from django.core.exceptions import ValidationError

# SignUp Form
class SignUpForm(forms.Form):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmpassword = cleaned_data.get("confirmpassword")

        if password and confirmpassword and password != confirmpassword:
            raise ValidationError("Passwords do not match.")

# SignIn Form
class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
