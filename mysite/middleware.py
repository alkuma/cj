from django.conf import settings
import re

class SubdomainsMiddleware:
    def process_request(self, request):
        domain_parts = request.get_host().split('.')
        if len(domain_parts) == 3 :
            request.subdomain = domain_parts[0]
            request.domain = '.'.join(domain_parts[1:])
            if request.subdomain.startswith('ghanti'):
                settings.ROOT_URLCONF = 'ghanti.urls'
            elif request.subdomain.startswith('taar'):
                settings.ROOT_URLCONF = 'taar.urls'
