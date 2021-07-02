from emarket.utils.mixins import ResponseGenericViewMixin
from django.contrib.auth import get_user_model
from rest_framework import generics, mixins

from .serializers import UserSerializer

User = get_user_model()


class UserListView(
        generics.ListAPIView,
        ResponseGenericViewMixin,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserViewSet(
        ResponseGenericViewMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
