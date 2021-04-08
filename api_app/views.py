from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from api_app import permissions
from api_app.Serializers import UserProfileSerializer
from api_app.models import UserProfile
from api_app.Serializers import UserMomentSerializer
from api_app.models import UserMoment

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.UserProfilePermission,)
    authentication_classes = (TokenAuthentication, )

class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserMomentViewSet(viewsets.ModelViewSet):
    queryset = UserMoment.objects.all()
    serializer_class = UserMomentSerializer
    permission_classes = (permissions.UserMomentPermission, )
    authentication_classes = (TokenAuthentication, )
