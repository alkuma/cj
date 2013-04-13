from django.db import models

# Create your models here.
class Chittha(models.Model):
    xml_url = models.CharField(max_length=2000)  #parital index on xml_url(191)
    html_url = models.CharField(max_length=2000)
    verified = models.BooleanField()
    kab_bana = models.DateTimeField(auto_now_add=True)
    kab_badla = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.xml_url

class Maal(models.Model):
    xml = models.TextField()
    kab_bana = models.DateTimeField(auto_now_add=True)
    kab_badla = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.xml
