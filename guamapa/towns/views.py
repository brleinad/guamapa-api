from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Town, AssistantMayor, SurveyQuestion, SurveyAnswer
from .serializers import TownSerializer, AssistantMayorSerializer, SurveyQuestionSerializer, SurveyAnswerSerializer
from ..permissions import IsStaffOrReadOnly, IsStaffAndAuthenticatedReadOnly


class TownViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves towns
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    permission_classes = (IsStaffOrReadOnly,)

class AssistantMayorViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves assistant mayors
    """
    queryset = AssistantMayor.objects.all()
    serializer_class = AssistantMayorSerializer
    permission_classes = (IsStaffAndAuthenticatedReadOnly,)

class SurveyQuestionViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves survey questions
    """
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer
    permission_classes = (IsStaffAndAuthenticatedReadOnly,)

class NestedSurveyAnswerViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves survey answers
    """
    queryset = SurveyAnswer.objects.all()
    serializer_class = SurveyAnswerSerializer
    permission_classes = (IsStaffAndAuthenticatedReadOnly,)

    def get_queryset(self):
        return SurveyAnswer.objects.filter(town=self.kwargs['town_pk'])


class SurveyAnswerViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves survey answers
    """
    queryset = SurveyAnswer.objects.all()
    serializer_class = SurveyAnswerSerializer
    permission_classes = (IsStaffAndAuthenticatedReadOnly,)