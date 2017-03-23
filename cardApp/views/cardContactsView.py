from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from cardApp.serializers import *
from cardApp.models import *
from django.shortcuts import render


class ContactsViewSet(viewsets.ModelViewSet):

    serializer_class = cardContactsSerializer.ContactsSerializer

    def get_queryset(self): 
    	queryset = cardModel.Contacts.objects.filter(user = self.request.user)
    	return queryset
