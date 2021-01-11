from rest_framework.viewsets import ModelViewSet

from burger_api.models import UserProfile
from burger_api.serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
