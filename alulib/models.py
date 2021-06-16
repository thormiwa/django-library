from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username', ]
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class BaseInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseInfo):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Book(BaseInfo):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()
    author = models.ManyToManyField(Author)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

class Rent(models.Model):
    reason = models.TextField()
    return_date = models.DateField(blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Review(models.Model):
    comment = models.TextField()
    rate = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

