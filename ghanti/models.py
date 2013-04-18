# This file is part of Chitthajagat.
#
# Chitthajagat is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Chitthajagat is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Chitthajagat.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models

# Master list of chittha's
class Chittha(models.Model):
    xml_url = models.CharField(max_length=2000)  #parital index on xml_url(191)
    html_url = models.CharField(max_length=2000)
    verified = models.BooleanField()
    kab_bana = models.DateTimeField(auto_now_add=True)
    kab_badla = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.xml_url

# all pings from PubSubHubBub are dumpted here before parsing and storing
class Maal(models.Model):
    xml = models.TextField()
    kab_bana = models.DateTimeField(auto_now_add=True)
    kab_badla = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.xml

# parsed Maal == lekh
class Lekh(models.Model):
    chittha_html_url = models.CharField(max_length=2000)
    shirshak = models.CharField(max_length = 4*80)
    lekh = models.TextField()
    kab_chhapa = models.DateTimeField()
    kab_badla = models.DateTimeField()
    url = models.CharField(max_length = 2000)

    def __unicode__(self):
        return self.url
