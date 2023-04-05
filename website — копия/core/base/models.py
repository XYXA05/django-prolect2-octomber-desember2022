import uuid
from email.policy import default
from enum import auto
from pydoc import describe
from unittest.util import _MAX_LENGTH

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    name = models.CharField(null=True, max_length=100)
    hackathon_participent = models.BooleanField(default=True, null=True)
    avatar = ResizedImageField(size=[100,100], default='default_icon.png')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    instagram = models.URLField(max_length=100, null=True, blank=True)
    telegram_username = models.CharField(null=True, blank=True, max_length=50)
    youtube = models.URLField(max_length=100, null=True, blank=True)



class Event(models.Model):
    name = models.CharField(null=True, max_length=50)
    describtion = models.TextField(null=True, blank=True)
    data_create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    participans = models.ManyToManyField(User, blank=True, related_name='events')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='submissions')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    details = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.event) + ' ---- ' + str(self.participant)

    