from rest_framework import serializers

from reporter.models import ReportedFile
from loader.models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'

class ReportedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedFile
        fields = '__all__'