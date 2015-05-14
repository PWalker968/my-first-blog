from django.conf.urls import include, url 
from import . import views

urlpatterns = [
	url(r'^$', views.post_list),
	]