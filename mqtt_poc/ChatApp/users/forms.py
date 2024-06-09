from typing import Any

from django import forms

from users.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(
        max_length=200, widget=forms.PasswordInput(attrs={"type": "password"})
    )


class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")

    def save(self, commit: bool = ...) -> Any:
        user = self.Meta.model.objects.create_user(**self.cleaned_data)
        return user
