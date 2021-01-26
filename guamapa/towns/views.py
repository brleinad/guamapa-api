from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Town, AssistantMayor
from .serializers import TownSerializer, AssistantMayorSerializer
from ..permissions import IsStaffOrReadOnly


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
    permission_classes = (IsStaffOrReadOnly,)

    def get_queryset(self):
        return AssistantMayor.objects.filter(town=self.kwargs['town_pk'])
    


