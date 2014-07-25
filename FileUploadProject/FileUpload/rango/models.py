from django.db import models

class UserName(models.Model):
	name = models.CharField(max_length=128, unique=False)
	
	def __unicode__(self):
		return self.name

class UserEmail(models.Model):
	user_name = models.OneToOneField(UserName)
	email = models.CharField(max_length=128, unique=False)
	
	def __unicode__(self):
		return self.email