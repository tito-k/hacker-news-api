from django.db import models
from django.core.validators import int_list_validator

from hacker_news_api.choices import items_choices

from django_unixdatetimefield import UnixDateTimeField

class Base(models.Model):
    id = models.PositiveIntegerField(unique=True, editable=False)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    type = models.CharField(max_length=20, choices=items_choices)
    by = models.CharField(max_length=255, null=True, blank=True)
    time = UnixDateTimeField()
    dead = models.BooleanField(null=True, blank=True)
    kids = models.CharField(validators=int_list_validator, null=True, blank=True)
    
class Job(models.Model):
    id = models.PositiveIntegerField(unique=True, editable=False)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    type = models.CharField(max_length=20, choices=items_choices)
    by = models.CharField(max_length=255, null=True, blank=True)
    time = UnixDateTimeField()
    dead = models.BooleanField(null=True, blank=True)
    kids = models.CharField(validators=int_list_validator, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    
class Story(models.Model):
    id = models.PositiveIntegerField(unique=True, editable=False)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    type = models.CharField(max_length=20, choices=items_choices)
    by = models.CharField(max_length=255, null=True, blank=True)
    time = UnixDateTimeField()
    dead = models.BooleanField(null=True, blank=True)
    kids = models.CharField(validators=int_list_validator, null=True, blank=True)
    descendants = models.PositiveIntegerField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    
class Comment(models.Model):
    id = models.PositiveIntegerField(unique=True, editable=False)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    type = models.CharField(max_length=20, choices=items_choices)
    by = models.CharField(max_length=255, null=True, blank=True)
    time = UnixDateTimeField()
    dead = models.BooleanField(null=True, blank=True)
    kids = models.CharField(validators=int_list_validator, null=True, blank=True)
    parent = models.PositiveIntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

class Poll(models.Model):
    id = models.PositiveIntegerField(unique=True, editable=False)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    type = models.CharField(max_length=20, choices=items_choices)
    by = models.CharField(max_length=255, null=True, blank=True)
    time = UnixDateTimeField()
    dead = models.BooleanField(null=True, blank=True)
    kids = models.CharField(validators=int_list_validator, null=True, blank=True)
    parts = models.CharField(validators=int_list_validator, null=True, blank=True)
    descendants = models.PositiveIntegerField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    
class PollOption(models.Model):
    id = models.PositiveIntegerField(unique=True, editable=False)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    type = models.CharField(max_length=20, choices=items_choices)
    by = models.CharField(max_length=255, null=True, blank=True)
    time = UnixDateTimeField()
    dead = models.BooleanField(null=True, blank=True)
    kids = models.CharField(validators=int_list_validator, null=True, blank=True)
    parent = models.PositiveIntegerField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)