from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from cardApp.serializers import *
from cardApp.models import *
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = profileModel.Profile.objects.all()
    serializer_class = profileSerializer.ProfileSerializer