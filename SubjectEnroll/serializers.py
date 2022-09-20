from pyexpat import model
from rest_framework import serializers 
from SubjectEnroll.models import TestData

class TestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestData
        fields = ('id', 'word')