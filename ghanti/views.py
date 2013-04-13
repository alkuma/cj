from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests, sys
from django.conf import settings
from ghanti.models import Chittha, Maal
import logging
import feedparser

logger = logging.getLogger(__name__)

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

def hai(xml):
    exists = Chittha.objects.filter(xml_url__exact=xml).count()
    if exists == 0:
        return False
    return True

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

def feedparse(x):
    f=feedparser.parse(x)
    #lekh shirshak 
    for i in f.feed.links[:]:
        if i['href'] == 'text/html' and i['rel'] == 'alternate':
            lekh.chittha_url = i['href']    
    lekh.chittha_shirshak = f.feed.title
    lekh.chittha.lekhak = f.feed.author
    lekh.chittha.chippi = f.feed.tags
    for e in f.entries[:]:
        lekh.shirshak = e.title
        lekh.lekh = e.content
        lekh.kab_badla = e.updated
        lekh.chippi = e.tags
        lekh.url = e.feedburner_origlink #what if no feedburner?
        lekh.summary = e.summary
        lekh.content = e.content
