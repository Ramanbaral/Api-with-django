from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from receipe.serializers import Tagserializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)
    queryset = Tag.objects.all()
    serializer_class = Tagserializers

    def get_queryset(self):

        return self.queryset.filter(self.request.user).order_by('-name')
