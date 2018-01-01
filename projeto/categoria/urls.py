from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView


urlpatterns = [
	url(r'list/$', CategoriaListView.as_view(), name='categoria_list'),
	url(r'cad/$', CategoriaCreateView.as_view(), name='categoria_create'),
	url(r'(?P<pk>\d+)/$', CategoriaUpdateView.as_view(), name='categoria_update'),
]

#url para arquivos de media quando em desenvolvimento
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)