from django.db import models
from . import cardModel
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	card = models.ManyToManyField(cardModel.Card)
