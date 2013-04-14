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

from django.conf import settings
import re

# TODO magic number 3, needs to be replaced by a settings.py parameter
class SubdomainsMiddleware:
    def process_request(self, request):
        domain_parts = request.get_host().split('.')
        if len(domain_parts) == 3 : #eg ghanti.example.com
            request.subdomain = domain_parts[0]
            request.domain = '.'.join(domain_parts[1:])
            if request.subdomain.startswith('ghanti'):
                settings.ROOT_URLCONF = 'ghanti.urls'
            elif request.subdomain.startswith('taar'):
                settings.ROOT_URLCONF = 'taar.urls'
