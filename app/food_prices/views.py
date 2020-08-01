from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Country
from .permissions import IsUserOrReadOnly
from .serializers import CountrySerializer


class ChickenViewSet(ModelViewSet):
    """
    Updates and retrieves user accounts
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsUserOrReadOnly, AllowAny)
