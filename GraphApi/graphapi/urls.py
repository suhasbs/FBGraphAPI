from django.conf.urls import url
from . import views

app_name = 'graphapi'


urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^get_access_token/$', views.get_access_token, name='access_token'),
	url(r'^get_my_info/$',views.get_my_info, name='myinfo'),
	url(r'^search_user/$',views.search_user, name='search'),
	url(r'^get_photo_ids/$', views.get_photo_ids, name='photo_ids')
]
