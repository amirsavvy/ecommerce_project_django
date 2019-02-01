from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                 "placeholder": "Your full Name"
                 })
                 )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
             "placeholder": "Your Email"
             }))
    content = forms.CharField(
    widget=forms.Textarea(
        attrs={
            "class": "form-control",
             "placeholder": "Your Message"
             })
    )




    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.")
        return email



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
            widget=forms.PasswordInput,label='Confirm password' )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        temp = User.objects.filter(username=username)
        if temp.exists():
            raise forms.ValidationError('Sorry this username: ' + username + ' is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        temp_user = User.objects.filter(email=email)
        if temp_user.exists():
            raise forms.ValidationError('Sorry this email: ' + email + ' is taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Password not matched!')
        return data
