from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageUploadView, ResumeUploadView

router = DefaultRouter()
router.register(r'images', ImageUploadView, basename='image-upload')
router.register(r'resumes', ResumeUploadView, basename='resume-upload')

urlpatterns = [
    path('', include(router.urls)),
]
