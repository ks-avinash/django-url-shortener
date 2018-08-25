# Create your views here.
import json
import random
import string

import tldextract
from django.conf import settings
from django.db.models import Q
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

    extracted = tldextract.extract(url)
    domain = "{}.{}".format(extracted.domain, extracted.suffix)
    url_present = ShortURL.objects.get(Q(url=url) | Q(url__endswith=domain))
    if url_present:
        short_url = url_present.shortened_url
    else:
        u_id = get_short_code()
        short_url = settings.SITE_URL + "/" + u_id
        b = ShortURL(url=url, unique_id=u_id, shortened_url=short_url)
        b.save()
    response = {'status': "success", 'short_url': short_url}
    return HttpResponse(json.dumps(response), content_type='application/json', status=200)


@csrf_exempt
@api_view(['GET'])
def shortened_urls_list(request):
    all_short_urls = ShortURL.objects.values_list('shortened_url', flat=True)

    if all_short_urls.count() > 0:
        urls = [str(x) for x in all_short_urls]
        response = {'status': "success", 'short_urls': urls}
    else:
        response = {'status': "error", 'message': "short urls not found"}
    return HttpResponse(json.dumps(response), content_type='application/json', status=200)


@csrf_exempt
@api_view(['POST'])
def get_original_url(request):
    try:
        params = json.loads(request.body.decode('utf-8'))
        short_url = params['short_url']
    except KeyError as e:
        response = {'status': "error", 'message': "error occurs"}
        return HttpResponse(json.dumps(response), "application/json", status=400)

    try:
        url_object = ShortURL.objects.get(shortened_url=short_url)
        original_url = url_object.url
        response = {'status': "success", 'original_url': original_url}
    except ShortURL.DoesNotExist:
        response = {'status': "error", 'message': "original url not found"}

    return HttpResponse(json.dumps(response), content_type='application/json', status=200)


@csrf_exempt
@api_view(['POST'])
def delete_shortened_url(request):
    try:
        params = json.loads(request.body.decode('utf-8'))
        short_url = params['short_url']
    except KeyError as e:
        response = {'status': "error", 'message': 'error occurs'}
        return HttpResponse(json.dumps(response), 'application/json', status=400)

    url_object = ShortURL.objects.filter(shortened_url=short_url)
    if url_object:
        url_object.delete()
        response = {'status': 'success', 'message': 'url successfully deleted'}
    else:
        response = {'status': 'error', 'message': 'short url not exists to remove'}

    return HttpResponse(json.dumps(response), content_type='application/json', status=200)


@csrf_exempt
@api_view(['POST'])
def read_urls_csv(request):
    try:
        file = request.FILES['csv_file']
    except KeyError as e:
        response = {'status': "error", 'message': 'error occurs'}
        return HttpResponse(json.dumps(response), 'application/json', status=400)
    decoded_file = file.read().decode('utf-8').splitlines()
    converted_urls = []
    for url in decoded_file:
        extracted = tldextract.extract(url)
        domain = "{}.{}".format(extracted.domain, extracted.suffix)
        url_present = ShortURL.objects.filter(Q(url=url) | Q(url__endswith=domain))
        if url_present:
            short_url = url_present.shortened_url
            converted_urls.append(short_url)
        else:
            u_id = get_short_code()
            short_url = settings.SITE_URL + "/" + u_id
            b = ShortURL(url=url, unique_id=u_id, shortened_url=short_url)
            b.save()
            converted_urls.append(short_url)

    response = {'status': 'success', 'converted urls': converted_urls}
    return HttpResponse(json.dumps(response), content_type='application/json', status=200)
