from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cardApp.models import *

class ContactsSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = cardModel.Contacts
		fields = ('card', 'user')
		read_only_fields = ('user', 'card')
		depth = 1

	def create(self, validated_data):
		print('val data', validated_data)
		print('self.context[request].data', self.context['request'].data)

		selfContext = self.context['request'].data['email']
		currentUser = self.context['request'].user
		requested_card = cardModel.Card.objects.get(email=selfContext)
		# card = cardModel.Card.objects.get(user=currentUser) 
		
		
		currentCardModel = cardModel.Contacts.objects.create(user=currentUser, card=requested_card)
		return currentCardModel
		
		


		
	
