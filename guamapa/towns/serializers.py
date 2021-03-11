from rest_framework import serializers
from .models import Town, AssistantMayor, SurveyQuestion, SurveyAnswer, Business, PointOfInterest


class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = '__all__'


class AssistantMayorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssistantMayor
        fields = '__all__'

    

class SurveyQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestion
        fields = '__all__'


class SurveyAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyAnswer
        fields = '__all__'
    

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = '__all__'


class PointOfInterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointOfInterest
        fields = '__all__'