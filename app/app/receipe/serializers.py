from rest_framework import serializers

from core.models import Tag


class Tagserializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id')
