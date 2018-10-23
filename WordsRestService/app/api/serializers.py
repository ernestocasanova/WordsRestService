from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import modelform_factory
from app.utils.colors import Colors
from app.api.models import Words
from enum import Enum
import random

class WordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Words
        fields = ('id', 'color', 'words', 'countwords', 'created', 'updated')

    def create(self, validated_data):
        """Custom create method to allow manipulate the hexa color in count of words when creating"""
        form = modelform_factory(Words, fields=('color', 'words', 'countwords'))
        words = validated_data.get('words')
        count = len(words.split())
        color = Colors.get_color(words, count)
        json = { 'color': color, 'words': words, 'countwords': count }
        populated_form = form(data=json)
        if populated_form.is_valid():
            return populated_form.save()

    def update(self, instance, validated_data):
        """Custom update method to allow manipulate the hexa color in count of words when creating"""
        words = validated_data.get('words')
        count = len(words.split())
        color = Colors.get_color(words, count)
        instance.color = Colors.get_color(words, count)
        instance.countwords = count
        instance.words = words
        instance.save()
        return instance