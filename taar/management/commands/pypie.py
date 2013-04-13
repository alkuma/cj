from django.core.management.base import BaseCommand, CommandError
import feedparser
from ghanti.models import Maal

class Command(BaseCommand):
    args = 'xml_file_name'
    help = 'parses the feeds received from hub'

    def handle(self, *args, **options):
#        Get the list of maal 
#        Obtain the parse one by one and store
#        delete from maal
        for x in Maal.objects.all():
            f = feedparser.parse(x.xml)     
#            f.lekh_url
#            f.chittha_name
#            f.chittha_url
#            f.lekh_shirshak
#            f.lekhak
#            f.chippi
#            f.kab_chhapa
#            f.kab_mila
            # store in lekh
            # delete maal
