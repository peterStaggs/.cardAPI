from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cardApp.models import *

class CardSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = cardModel.Card
		fields = ('user', 'contacts', 'full_name', 'phone_number', 'title', 'business', 'email', 'linkedin', 'social_media')
		read_only_fields = ('user',)
		depth = 1


	def create(self, validated_data):
		newUser = self.context['request'].user
		card = cardModel.Card(
			user=newUser,
			full_name = validated_data['full_name'],
			phone_number = validated_data['phone_number'],
			title = validated_data['title'],
			business = validated_data['business'],
			email = validated_data['email'],
			linkedin = validated_data['linkedin'],
			social_media = validated_data['social_media'],
			)
		card.save()
		return card


