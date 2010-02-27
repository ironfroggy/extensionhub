from django.db import models

from forkws.models import Fork
 

# Create your models here.
class JetPack(models.Model):
	"""Represents a JetPack extension for Firefox"""
	
	name = models.CharField(max_length=255)
	file_name = models.CharField(max_length=255)
	fork = models.ForeignKey(Fork)
		
