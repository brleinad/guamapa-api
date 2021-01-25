from rest_framework import serializers
from .models import Town, AssistantMayor


class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = '__all__'
        # fields = ['id', 'name', 'location', 'elevation', 'population', 'category']


class AssistantMayorSerializer(serializers.ModelSerializer):


    class Meta:
        model = AssistantMayor
        fields = '__all__'