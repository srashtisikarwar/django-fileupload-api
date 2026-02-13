from rest_framework import serializers
from .models import ImageUpload, ResumeUpload


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = '__all__'

    def validate_image(self, value):
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Image size exceeds 5MB.")
        return value


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUpload
        fields = '__all__'

    def validate_resume(self, value):
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("File size exceeds 5MB.")
        return value
