from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=200)
	desc = models.TextField()
	amount = models.IntegerField()