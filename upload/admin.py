from django.contrib import admin
from .models import ImageUpload, ResumeUpload
from rest_framework import serializers
# Register your models here.

admin.site.register(ImageUpload)
admin.site.register(ResumeUpload)