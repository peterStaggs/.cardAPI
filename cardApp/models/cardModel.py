from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
	user = models.ForeignKey(User)
	contacts = models.ManyToManyField(User, through='Contacts')
	full_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=25)
	title = models.CharField(max_length=200)
	business = models.CharField(max_length=200)
	email = models.EmailField(max_length=254, unique = True)
	linkedin = models.URLField(max_length=200, null=True, blank=True)
	social_media = models.URLField(max_length=200, null=True, blank=True)

	class Meta:
		ordering = ('full_name',)

	def __str__(self):
		return '{} {} {} {} {} {} {} {}'.format(self.user, self.contacts, self.full_name, self.phone_number, self.title, self.business, self.email, self.linkedin, self.social_media)

class Contacts(models.Model): 
	card = models.ForeignKey(Card)
	user = models.ForeignKey(User)


