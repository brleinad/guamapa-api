from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Town
from .serializers import TownSerializer


class TownViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves towns
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    permission_classes = (AllowAny,)


class TownCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates towns
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    permission_classes = (IsAdminUser,)
    
