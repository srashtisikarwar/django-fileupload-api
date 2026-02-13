from django.db import models
from django.core.validators import FileExtensionValidator


class ImageUpload(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Image Upload'
        verbose_name_plural = 'Image Uploads'


class ResumeUpload(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    resume = models.FileField(
        upload_to='resume/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Resume Upload'
        verbose_name_plural = 'Resume Uploads'
