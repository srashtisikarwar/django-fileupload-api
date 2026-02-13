from rest_framework.viewsets import ModelViewSet
from .models import ImageUpload, ResumeUpload
from .serializers import ImageUploadSerializer, ResumeUploadSerializer
from django_filters.rest_framework import DjangoFilterBackend



class ImageUploadView(ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class ResumeUploadView(ModelViewSet):
    queryset = ResumeUpload.objects.all()
    serializer_class = ResumeUploadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
