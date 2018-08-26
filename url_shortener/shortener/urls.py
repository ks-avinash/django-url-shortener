from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^(?P<short_id>\w{6})$', views.redirect_original, name='redirect_original'),
    url(r'^shortened-urls$', views.get_shortened_url, name='shorten_url'),
    url(r'^all-shortened-urls$', views.shortened_urls_list, name='shortened_urls_list'),
    url(r'^original-urls$', views.get_original_url, name='get_original_url'),
    url(r'^delete-urls$', views.delete_shortened_url, name='delete_shortened_url'),
    url(r'^short-urls-from-csv$', views.read_urls_csv, name='read_urls_csv'),

]
