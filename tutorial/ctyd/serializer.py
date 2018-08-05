# coding=utf-8
from rest_framework import serializers
from . import models
class CtydSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DataCtyd
        fields=('')
