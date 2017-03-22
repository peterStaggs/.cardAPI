from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from cardApp.serializers import *
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json 

@csrf_exempt
def register(request): 
	req_body = json.loads(request.body.decode())
	username = req_body['username']
	password = req_body['password']
	new_user = User.objects.create_user(
		username = username, 
		password = password
		)

	data = json.dumps({"success": True})
	return HttpResponse(data, content_type="application/json")