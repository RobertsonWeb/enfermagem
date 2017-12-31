from django.conf.urls import url

from .views import MidiaListView, MidiaCreateView
from .views import MidiaUpdateView, MidiaDeleteView


urlpatterns = [
	url(r'list/$', MidiaListView.as_view(), name='midia_list'),
	url(r'cad/$', MidiaCreateView.as_view(), name='midia_create'),
	url(r'(?P<pk>\d+)/$', MidiaUpdateView.as_view(), name='midia_update'),
	url(r'(?P<pk>\d+)/delete/$', MidiaDeleteView.as_view(), name='midia_delete'),
]
