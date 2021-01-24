from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Town
from .serializers import TownSerializer
from ..permissions import IsStaffOrReadOnly


class TownViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves towns
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    permission_classes = (IsStaffOrReadOnly,)
