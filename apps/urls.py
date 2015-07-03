from django.conf.urls import patterns, url
from apps import views

urlpatterns = patterns('',

	# Vista
	url(r'^$', views.IndexView.as_view(), name='index'),
)