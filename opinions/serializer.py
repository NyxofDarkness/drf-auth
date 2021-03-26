
from rest_framework import serializers
from .models import Opinions

class OpinionSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
           'id',
           'author',
           'title',
           'body',
           'created',
       )
       model = Opinions

