from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Town
from .serializers import TownSerializer


class TownViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves towns
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    permission_classes = (AllowAny,)


class TownEditViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Creates towns
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    permission_classes = (IsAdminUser,)
    
