from rest_framework import serializers
from .models import Town


class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = ['id', 'name', 'location']