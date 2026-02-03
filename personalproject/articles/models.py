from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Page(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.title
    def getAbsoluteUrl(self):
        return reverse(
            'articles:pageDetail',
            args=[self.id]
        )
    
class Movie(Page):
    release = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

class Monster(Page):
    debut = models.CharField(max_length=250)
    latest = models.CharField(max_length=250)