from django.conf.urls import url

from .views import InstituicaoListView, InstituicaoCreateView
from .views import InstituicaoUpdateView, InstituicaoDeleteView


urlpatterns = [
	url(r'list/$', InstituicaoListView.as_view(), name='instituicao_list'),
	url(r'cad/$', InstituicaoCreateView.as_view(), name='instituicao_create'),
	url(r'(?P<pk>\d+)/$', InstituicaoUpdateView.as_view(), name='instituicao_update'),
	url(r'(?P<pk>\d+)/delete/$', InstituicaoDeleteView.as_view(), name='instituicao_delete'),
]
