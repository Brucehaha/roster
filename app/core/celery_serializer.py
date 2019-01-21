from rest_framework import serializers
from . import models


class CelerySerializer(serializers.HyperlinkedModelSerializer):
    """Serialize the TaskCelery object"""
    class Meta:
        model = models.CeleryTask
        fields = ('id', 'function', 'task', 'result')
        read_only_fields = ('id',)
