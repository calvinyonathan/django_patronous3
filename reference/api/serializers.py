from rest_framework import serializers
from ..models import Reference

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id','title','description','author','link']
        
