from django.contrib.postgres.fields import ArrayField
from django.db import models
from django_unixdatetimefield import UnixDateTimeField

from hacker_news_api.choices import items_choices

class Base(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    type = models.CharField(max_length=20, choices=items_choices)
    by = models.CharField(max_length=255, null=True, blank=True, default=None)
    time = UnixDateTimeField(null=True, blank=True)
    dead = models.BooleanField(null=True, blank=True, default=False)
    kids = ArrayField(models.PositiveIntegerField(null=True, blank=True), null=True, blank=True, default=None)
    parts = ArrayField(models.PositiveIntegerField(null=True, blank=True), null=True, blank=True, default=None)
    parent = models.PositiveIntegerField(null=True, blank=True, default=None)
    text = models.TextField(null=True, blank=True, default=None)
    descendants = models.PositiveIntegerField(null=True, blank=True, default=None)
    score = models.PositiveIntegerField(null=True, blank=True, default=None)
    url = models.URLField(max_length=512, null=True, blank=True, default=None)
    title = models.CharField(max_length=500, null=True, blank=True, default=None)
    is_from_hacker_news = models.BooleanField(default=True)
    is_top = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        ordering = ["-time"]
    