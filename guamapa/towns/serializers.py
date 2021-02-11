from rest_framework import serializers
from .models import Town, AssistantMayor, SurveyQuestion, SurveyAnswer


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
    