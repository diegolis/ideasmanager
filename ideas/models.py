from __future__ import unicode_literals
import datetime

from django.db import models


class Idea(models.Model):
	datetime = models.DateTimeField(default=datetime.datetime.now)
	content = models.TextField()
	title = models.CharField(max_length=500, null=True, blank=True)
	source = models.CharField(max_length=500, null=True, blank=True)

	archived = models.BooleanField(default=False)

	def __unicode__(self):
		return self.content[:25]

