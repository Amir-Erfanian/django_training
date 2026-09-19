from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='posts',
    )

    def __str__(self):
        return self.title

    def short_title(self):
        return self.title[:20]

    def clean(self):
        if self.title.strip().lower() == self.content.strip().lower():
            raise ValidationError(
                'Title and content should not be identical.'
            )

    class Meta:
        ordering = ['-created_at']