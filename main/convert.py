import hashlib
import json
from .views import HOST
from .models import Link
from django.http import HttpResponseBadRequest, HttpResponse
import validators


def convert(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    error = ''
    duplicate = False
    absolute_url = ''
    url = request.POST.get('original_url')

    if validators.url(url):
        url_bytes = url.encode('utf-8')
        sha = hashlib.sha1(url_bytes)
        shortlink_url = sha.hexdigest()
        shortlink_url = shortlink_url[:6]
        absolute_url = str(HOST + 'link/' + shortlink_url + '/')
        result, created = Link.objects.get_or_create(
            original_url=url,
            shortlink_url=shortlink_url, )
        if not created:
            duplicate = 'already exists'
    else:
        error = 'Incorrect link format'

    if error:
        response = {
            'error': error
        }
        return HttpResponseBadRequest(json.dumps(response), content_type="application/json")

    response = {
        'shortlink_url': absolute_url,
        'duplicate': duplicate
    }
    return HttpResponse(json.dumps(response), content_type="application/json")
