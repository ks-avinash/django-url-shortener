from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^(?P<short_id>\w{6})$',views.redirect_original, name='redirect_original'),
    url(r'^shorten_url$', views.shorten_url, name='shorten_url'),
    url(r'^shortened_urls_list$', views.shortened_urls_list, name='shortened_urls_list'),
    url(r'^get_original_url$', views.get_original_url, name='get_original_url'),
    url(r'^delete_shortened_url', views.delete_shortened_url, name='delete_shortened_url'),
    url(r'^read_urls_csv', views.read_urls_csv, name='read_urls_csv'),

]

