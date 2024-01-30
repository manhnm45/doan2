from rest_framework import serializers
from .models import weith

class Scaleserializer(serializers.ModelSerializer):
    class Meta:
        model = weith
        fields = '__all__'