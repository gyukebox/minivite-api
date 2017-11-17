from rest_framework import serializers
from .models import *


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectionModel
        fields = ('body', 'num_people')


class PollSerializer(serializers.ModelSerializer):
    selections = SelectionSerializer(many=True, required=True, read_only=False)

    class Meta:
        model = PollModel
        fields = ('title', 'selections')


class PollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollModel
        fields = ('title', )
