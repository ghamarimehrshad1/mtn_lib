from django import forms
from accounting.models import CustomUser

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class ProfileForm(forms.ModelForm):
    username = forms.CharField(required=False)

    class Meta:
        model=CustomUser
        exclude = ('debt', 'user', )


class ContactUsForm(forms.Form):
    name=forms.CharField(max_length=40)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea())