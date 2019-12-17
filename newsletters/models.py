from django.utils.text import slugify
from pyexpat import model
from django.db import models
# Create your models here.
from rest_framework_simplejwt.state import User

FREQUENCY = (
    ('daily', 'Diario'),
    ('weekly', 'Semanal'),
    ('monthly', 'Mensual')
)

class Tags(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tags, self).save(*arg, **kwargs)

    class Meta:
        ordering = ('-created_at',)

class Newsletter(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    image = models.ImageField()
    target = models.IntegerField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY, default='monthly')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tags)
    @property
    def subscribed(self):
        return 10

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)

