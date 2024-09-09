from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateField()

    STATUS_CHOICES = [
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='disponible')

    borrowed_by = models.ManyToManyField(
        User, blank=True, related_name='borrowed_books')

    def __str__(self):
        return self.title
