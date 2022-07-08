import json
import random
import string

from django.conf import settings

# from django.core.context_processors import csrf
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response

from .models import Urls


def index(request: HttpRequest) -> HttpResponse:
    c = {}
    c.update(csrf(request))
    return render_to_response('shortenersite/index.html', c)


def redirect_original(request: HttpRequest, short_id: str) -> HttpResponse:
    url = get_object_or_404(Urls, pk=short_id)
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)


def shorten_url(request: HttpRequest) -> HttpResponse:
    url = request.POST.get("url", '')
    if not (url == ''):
        short_id = get_short_code()
        b = Urls(httpurl=url, short_id=short_id)
        b.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(
            json.dumps(response_data), content_type="application/json"
        )
    return HttpResponse(
        json.dumps({"error": "error occurs"}), content_type="application/json"
    )


def get_short_code() -> str:
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        # try:
        #     temp = Urls.objects.get(pk=short_id)
        # except:
        return short_id
