from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'original_file', 'optimized_file', 'status', 'created_at', 'updated_at']
