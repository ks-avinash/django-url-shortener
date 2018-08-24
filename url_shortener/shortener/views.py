# Create your views here.
import json
import random
import string

from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from shortener.models import ShortURL


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        random_string = ''.join(random.choice(char) for x in range(length))
        try:
            temp = ShortURL.objects.get(pk=random_string)
            return temp
        except:
            return random_string


def redirect_original(request, short_id):
    short_url = get_object_or_404(ShortURL, pk=short_id)
    short_url.count += 1
    short_url.save()
    return HttpResponseRedirect(short_url.url)


@csrf_exempt
@api_view(['POST'])
def shorten_url(request):
    try:
        params = json.loads(request.body.decode('utf-8'))
        url = params['url']
    except KeyError as e:
        response = {'status': "error", 'message': "error occurs"}
        return HttpResponse(json.dumps(response), "application/json", status=400)

    try:
        url_present = ShortURL.objects.get(url=url)
        u_id = url_present.unique_id
    except ShortURL.DoesNotExist:
        u_id = get_short_code()
    b = ShortURL(url=url, unique_id=u_id)
    b.save()
    response = {'status': "success", 'short_url': settings.SITE_URL + "/" + u_id}
    return HttpResponse(json.dumps(response), content_type='application/json', status=200)
