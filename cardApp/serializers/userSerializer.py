from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cardApp.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('username', 'password')

	def create(self, validated_data):
		print(validated_data)
		user = User(
			username=validated_data['username']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user