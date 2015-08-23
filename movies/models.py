from django.db import models

# Create your models here.

class Films(models.Model):
	title = models.CharField(max_length=100, blank=False)
	release_year = models.IntegerField(blank=True)
	locations = models.CharField(max_length=200, blank=True)
	fun_facts = models.CharField(max_length=500, blank=True)
	production_company = models.CharField(max_length=200, blank=True)
	distributor = models.CharField(max_length=200, blank=True)
	director = models.CharField(max_length=100, blank=True)
	writer = models.CharField(max_length=100, blank=True)
	actor_1 = models.CharField(max_length=100, blank=True)
	actor_2 = models.CharField(max_length=100, blank=True)
	actor_3 = models.CharField(max_length=100, blank=True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	
	def __str__(self):              # __unicode__ on Python 2
		return self.title
