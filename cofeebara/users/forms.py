from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    user_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        user_email = self.cleaned_data.get("user_email")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(user_email=user_email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 일치하지 않습니다!"))
        except User.DoesNotExist:
            self.add_error("user_email", forms.ValidationError("계정이 존재하지 않습니다!"))


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_email', 'user_nickname', 'user_firstname', 'user_lastname')
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다!")
        else:
            return password1

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user_email = self.cleaned_data.get("user_email")
        password = self.cleaned_data.get("password")
        user.username = user_email
        user.set_password(password)
        user.save()
        # user_nickname = self.cleaned_data.get("user_nickname")
        # user_firstname = self.cleaned_data.get("user_firstname")
        # user_lastname = self.cleaned_data.get("user_lastname")
        # user = User.objects.create_user(user_email, user_email, password)
        # user.user_nickname = user_nickname
        # user.user_firstname = user_firstname
        # user.user_lastname = user_lastname
        # user.save()
