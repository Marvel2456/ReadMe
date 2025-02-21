from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Author, Reader


class ReaderSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'is_reader', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_reader = True
        if commit:
            user.save()
        return user

class AuthorSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'is_author', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_author = True
        if commit:
            user.save()
        return user


class ReaderUpdateForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'bio', 'profile_picture']

class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'bio', 'profile_picture']
