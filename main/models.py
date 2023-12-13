from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


class FightForm(forms.Form):
    user_number = forms.IntegerField(
        label='Ваша атака (от 1 до 10)',
        min_value=1,
        max_value=10,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


class FastFightForm(forms.Form):
    pass


class EmailForm(forms.Form):
    email = forms.EmailField(label="Введите ваш адрес электронной почты, чтобы получить результат боя",
                             required=True,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Ваш адрес электронной почты'}))


class SavePokemonInfo(forms.Form):
    pass


class Fight(models.Model):
    account_id = models.CharField(max_length=30, default='None')
    date = models.DateTimeField()
    round_count = models.IntegerField()
    pokemon_name = models.CharField(max_length=30)
    enemy_name = models.CharField(max_length=30)
    result = models.BooleanField()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class CodeConfirmationForm(forms.Form):
    code = forms.CharField()
