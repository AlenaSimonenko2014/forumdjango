from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Section(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return "Section: {0}".format(self.name)


class Topic(models.Model):
	name = models.CharField(max_length=60, unique=True)
	section = models.ForeignKey(Section)

	def __str__(self):
		return "Topic: {0}".format(self.name)


class Message(models.Model):
	text = models.TextField(blank=False)
	topic = models.ForeignKey(Topic)
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Message from {0} in [{1}] date ({2}): {3}...".format(str(self.user), self.topic, self.date.strftime("%d %B %Y (%H:%M:%S)"), self.text[:20])
