from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cardApp.models import *

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = profileModel.Profile
		fields = ('user', 'card')