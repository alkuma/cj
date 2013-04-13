from django.db import models

# Create your models here.
class Lekh(models.Model):
	lekh_url = models.CharField(max_length=2000)
	chittha_shirshak = models.CharField(max_length=80)
	chittha_url = models.CharField(max_length=2000)
	lekh_shirshak = models.CharField(max_length=80)
	lekhak = models.CharField(max_length=80)
	khatadhari = models.CharField(max_length=2000)
#	khatadhari_tasveer = models.CharField(max_length=2000)
	pathit = models.BooleanField()
	sajha = models.BooleanField()
#	chippi = models.IntegerField()
#	varg = models.CharField(max_length=2000)
#	chhavi = models.CharField(max_length=2000)
#	video = models.IntegerField()
#	audio = models.IntegerField()
	def __unicode__(self):
		return self.lekh_url
