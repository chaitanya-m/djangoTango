from django.db import models

class UserName(models.Model):
	name = models.CharField(max_length=128, unique=False)
	email = models.CharField(max_length=128, unique=False)
	picfile = models.FileField(upload_to='documents/%Y/%m/%d')
	def __unicode__(self):
		return self.name
	def file_link(self):
		if self.picfile:
			return "<a href='%s'>download</a>" % (self.picfile.url,)
		else:
			return "No attachment"

	file_link.allow_tags = True

class UserEmail(models.Model):
	user_name = models.OneToOneField(UserName)
	email = models.CharField(max_length=128, unique=False)
	
	def __unicode__(self):
		return self.email
		