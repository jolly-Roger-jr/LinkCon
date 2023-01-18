from django.contrib.auth.models import User

from .models import Link
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import AuthenticationForm


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ["original_url", "shortlink_url"]
        widgets = {
            "original_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку',
                'id': 'original_url_input'
            }),
        }

    def copy(self):
        pass


class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
