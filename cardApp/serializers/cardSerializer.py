from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cardApp.models import *

class CardSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = cardModel.Card
		fields = ('user', 'full_name', 'phone_number', 'title', 'business', 'email', 'linkedin', 'social_media')