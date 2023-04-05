from dataclasses import fields
from pyexpat import model
from statistics import mode
from unicodedata import name
from django.forms import ModelForm
from .models import Submission, User
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'avatar', 'bio', 'instagram', 'telegram_username', 'youtube']

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['details']

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password']