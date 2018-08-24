from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^(?P<short_id>\w{6})$',views.redirect_original, name='redirect_original'),
    url(r'^shorten_url/$', views.shorten_url, name='shorten_url'),
]

