from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import User

class LoginForm(forms.ModelForm):
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "비밀번호를 입력하세요"})
    )

    class Meta:
        model = User
        fields = ["user_email", "password"]
        widgets = {
            "user_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "이메일을 입력하세요"}),
        }
        labels = {
            "user_email": "이메일",
        }

    def clean(self):
        cleaned_data = super().clean()
        user_email = cleaned_data.get("user_email")
        password = cleaned_data.get("password")

        if user_email and password:
            self.user = authenticate(user_email=user_email, password=password)
            if self.user is None:
                raise forms.ValidationError("이메일 또는 비밀번호가 올바르지 않습니다.")
            elif not self.user.is_active:
                raise forms.ValidationError("이 계정은 비활성화되었습니다.")

        return cleaned_data

    def get_user(self):
        return self.user

class SignupForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['user_email','user_firstname', 'user_lastname', 'user_nickname']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['password2']