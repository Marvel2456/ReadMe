from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Author, Reader


class ReaderSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'is_reader', 'password1', 'password2']

class AuthorSignUpForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'is_author', 'password1', 'password2']


class ReaderUpdateForm(ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'bio', 'profile_pic']

class AuthorUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'bio', 'profile_pic']