from .models import OurModel
from rest_framework import serializers


class OurSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurModel
        fields = ['name', 'fname', 'text']
