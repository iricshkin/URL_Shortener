from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import UrlsForm
from .models import Urls


def home_view(request):
    template = 'shortenersite/index.html'
    context = {}
    context['form'] = UrlsForm()

    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = UrlsForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = (
                request.build_absolute_uri('/') + shortened_object.short_url
            )
            long_url = shortened_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url

            return render(request, template, context)

        context['errors'] = used_form.errors
        return render(request, template, context)


def redirect_url_view(request, shortened_part):

    try:
        shortener = Urls.objects.get(short_url=shortened_part)
        shortener.count += 1
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)

    except:
        raise Http404('Sorry this link is broken :(')
