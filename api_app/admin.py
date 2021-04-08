from django.contrib import admin
from api_app import models

admin.site.register(models.UserProfile)
admin.site.register(models.UserMoment)
