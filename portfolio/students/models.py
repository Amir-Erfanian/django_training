from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name