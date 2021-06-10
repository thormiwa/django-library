from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Rent)
admin.site.register(models.Review)