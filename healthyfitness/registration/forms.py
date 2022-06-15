from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, TextInput, EmailInput, PasswordInput


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', max_length=30, widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введите Email'}))
    password1 = CharField(label='Введите пароль', widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))
    password2 = CharField(label='Повторите пароль', widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Подтвердите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', max_length=30, widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password = CharField(label='Введите пароль',
                          widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))
                          