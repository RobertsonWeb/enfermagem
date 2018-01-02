from django.conf.urls import url

from .views import PerguntaListView, PerguntaCreateView
from .views import PerguntaUpdateView, PerguntaDeleteView


urlpatterns = [
	url(r'list/$', PerguntaListView.as_view(), name='pergunta_list'),
	url(r'cad/$', PerguntaCreateView.as_view(), name='pergunta_create'),
	url(r'(?P<pk>\d+)/$', PerguntaUpdateView.as_view(), name='pergunta_update'),
	url(r'(?P<pk>\d+)/delete/$', PerguntaDeleteView.as_view(), name='pergunta_delete'),
]