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

# individual articles
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
