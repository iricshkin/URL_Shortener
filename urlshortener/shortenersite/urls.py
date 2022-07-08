from django.urls import path

from . import views

app_name = 'shortenersite'

urlpatterns = [
    path(r'^$', views.index, name='home'),
    path(
        r'^(?P<short_id>\w{6})$',
        views.redirect_original,
        name='redirectoriginal',
    ),
    path(r'^makeshort/$', views.shorten_url, name='shortenurl'),
]
