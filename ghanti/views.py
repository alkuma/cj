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

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests, sys
from django.conf import settings
from ghanti.models import Chittha, Maal, Lekh
import logging
import feedparser

logger = logging.getLogger(__name__)

# add a chittha
@csrf_exempt
def jod(request):
    try:
        if (request.method == 'POST' and
          not hai(request.POST.get("hub.topic", ""))) :
            q = requests.post(settings.GHANTI_PUBLISH_URL, data= {
                   'hub.mode' : 'publish', 
                   'hub.url' : request.POST.get('hub.topic')})
            if q.status_code != 204:
                logger.debug(q.status_code)
                logger.debug(sys.exc_info())
                return HttpResponse(status = q.status_code,
                  content = sys.exc_info())
            r = requests.post(settings.GHANTI_HUB_URL, data = {
                   'hub.callback': settings.GHANTI_CALLBACK, 
                   'hub.topic':request.POST.get("hub.topic", ""),
                   'hub.mode': 'subscribe',
                   'hub.verify':'sync',
                   'hub.verify_token': settings.GHANTI_VERIFY_TOKEN})
            if r.status_code == 204:
                Chittha.objects.create(xml_url=request.POST.get("hub.topic"), 
                                       verified=True)
            return HttpResponse(status = r.status_code, content = r.status_code)
    except:
        logger.debug(sys.exc_info())
        return HttpResponse(status = 400, content = sys.exc_info())
    return HttpResponse(status = 200, content = 200)

# remove a chittha
@csrf_exempt
def tod(request):
    try:
        if (request.method == 'POST' and
          hai(request.POST.get("hub.topic", ""))) :
            r = requests.post(settings.GHANTI_HUB_URL, data = {
                   'hub.callback': settings.GHANTI_CALLBACK, 
                   'hub.topic':request.POST.get("hub.topic", ""),
                   'hub.mode': 'unsubscribe',
                   'hub.verify':'sync',
                   'hub.verify_token': settings.GHANTI_VERIFY_TOKEN})
            if r.status_code == 204:
                c = Chittha.objects.get(xml_url=request.POST.get("hub.topic")) 
                c.delete()
            return HttpResponse(status = r.status_code, content = r.status_code)
    except:
        logger.debug(sys.exc_info())
        return HttpResponse(status = 400, content = sys.exc_info())
    return HttpResponse(status = 200, content = 200)

# check for existence of a chittha
def hai(xml):
    exists = Chittha.objects.filter(xml_url__exact=xml).count()
    if exists == 0:
        return False
    return True

# confirm a subscription and recieve chittha updates
@csrf_exempt
def maal(request):
    if (request.method == 'GET' and
      request.GET.get("hub.verify_token") == settings.GHANTI_VERIFY_TOKEN):
        return HttpResponse(status=200, content_type="text/plain", content= 
              request.GET.get("hub.challenge"))
    if request.method == 'POST':
        Maal.objects.create(xml=request.body)
        feedparse(request.body)
        logger.debug(request.body)
        logger.debug('inside maal POST')
        return HttpResponse(status=200)
    return HttpResponse(status=403)

# parse the xml sent by PubSubHubBub
def feedparse(x):
    f=feedparser.parse(x)
    #lekh shirshak 
    # check if field exists before using each one
    # 
    for i in f.feed.links[:]:
        if i['href'] == 'text/html' and i['rel'] == 'alternate':
            chittha_url = i['href']    
    chittha_shirshak = f.feed.title
    chittha_lekhak = f.feed.author
    chittha_chippi = f.feed.tags
    for e in f.entries[:]:
        lekh = Lekh()
        lekh.shirshak = e.title
        lekh.lekh = e.summary
        lekh.kab_chhapa = e.published
        lekh.kab_badla = e.updated
        lekh.url = e.feedburner_origlink #what if no feedburner?
