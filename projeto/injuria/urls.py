from django.conf.urls import url

from .views import InjuriaListView, InjuriaCreateView
from .views import InjuriaUpdateView, InjuriaDeleteView


urlpatterns = [
	url(r'list/$', InjuriaListView.as_view(), name='injuria_list'),
	url(r'cad/$', InjuriaCreateView.as_view(), name='injuria_create'),
	url(r'(?P<pk>\d+)/$', InjuriaUpdateView.as_view(), name='injuria_update'),
	url(r'(?P<pk>\d+)/delete/$', InjuriaDeleteView.as_view(), name='injuria_delete'),
]