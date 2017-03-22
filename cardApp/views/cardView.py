from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from cardApp.serializers import *
from cardApp.models import *
from django.shortcuts import render


class CardViewSet(viewsets.ModelViewSet):

    queryset = cardModel.Card.objects.all()
    serializer_class = cardSerializer.CardSerializer