# Projeto de pesquisa de alunos dos cursos de Sistemas de Informação com o Programa de Mestrado em Saúde/Enfermagem

## Preparando o ambiente para desenvolvimento
> ***Ocorrência:*** A cada nova instalação do Sistema Operacional.

### Instalação do PIP (Python Index Package):
```shell
#Linux/Mac OSx:
sudo easy_install pip

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install python-pip
```

### Instalação do Virtualenv (Ferramenta gestora de ambientes Python virtualizados isolados):
```shell
#Linux/Mac OSx:
pip install virtualenv

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install python-virtualenv
```
### Instalação do GIT (Habilitar o Sistema Operacional para trabalhar com controle de versão GIT)
```shell
#Mac OS/x:
http://sourceforge.net/projects/git-osx-installer/

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install git
```

## Criação de um projeto exemplo:
> Passo a passo com principais atividades necessárias para iniciar um projeto. Consulte a documentação oficial do Django para mais detalhes https://www.djangoproject.com/start/

> ***Objetivo:*** Projeto Django rodando localmente, versionado com Git e distribuído na plataforma Github

```shell
#Criando o diretorio que conterá os recursos necessários para execução, desenvolvimento e distribuição do projeto
mkdir enfermagem

#Acessando o diretório principal
cd enfermagem

#Criando uma virtualenv com Python (ambiente isolado) - Ambiente localizado no diretório venv
virtualenv venv

#Ativando a virtualenv
source venv/bin/activate

#Instalando o Django 1.11 no ambiente isolado por meio do PIP
pip install Django==1.11

#Criando o arquivo de requirements do projeto
pip freeze > requirements.txt

#Iniciando um projeto Django
django_admin.py startproject projeto

#Acessando o diretório projeto
cd projeto

#Configurando a linguagem e data/hora do projeto. Edite o arquivo: projeto/settings.py
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

#Rodar a migração para criação das tabelas básicas do Django no Banco de dados
python manage.py migrate

#Criando o super usuário para acessar o Django Admin (Painel administrativo do site) via autenticação
python manage.py createsuperuser

#Criação de uma aplicação chamada core
python manage.py startapp core

#Criacao da view responsável pela exibição da home/index na app core
#edite o arquivo core/views.py e certifique-se que contenha:

from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import TemplateView

from utils.decorators import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'core/home.html'

#crie o home.html em core/templates/core/home.html (será preciso criar os diretórios)

#crie o arquivo urls.py em: core/urls.py Ele é responsável pela identificação da view responsável para cada URL pertencente a app core
touch core/urls.py

#edite o arquivo core/urls.py com o seguinte conteúdo:

from __future__ import unicode_literals
from django.conf.urls import url
from .views import HomeView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
]

#instale a app core no projeto editando o arquivo projeto/settings.py adicionando na lista INSTALLED_APPS como no exemplo:
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'core',
]

#habilite o gerenciador de URLs do projeto para trabalhar com as URLs da app core, para isto, edite o arquivo projeto/urls.py importando o urls do core, veja o exemplo:
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'', include('core.urls'))
]

#neste ponto a sua home já pode ser exibida no navegador

#rodando o servidor web de desenvolvimento (dentro do diretório projeto)
python manage.py runserver

#acessando via navegador
http://localhost:8000
```


## Criar um modelo para persistir no Banco de Dados, Instalando a app no Django Admin (Painel), Buscando os registros do modelo numa view e mostrando no HTML
```shell
#edite o arquivo core/models.py adicionando a classe do novo modelo conforme o exemplo:
class Produto(models.Model):
nome = models.CharField('Nome', max_length=70)
data_cadastro = models.DateTimeField('data do cadastramento', auto_now_add=True)
ativo = models.BooleanField('Ativado', default=True)

def __unicode__(self):
return self.nome

class Meta:
ordering = ['nome']
verbose_name = 'Produto'
verbose_name_plural = 'Produtos'

#comando no shell criar o script para migração do Banco de Dados dos modelos da app core (script que cria as tabelas necessárias para atender o modelo especificado)
python manage.py makemigrations core

#comando no shell para rodar as migrações da app core no Banco de Dados
python manage.py migrate core

#adicionar o modelo Produto da app core no Django Admin, edite o arquivo core/admin.py adicionando o que segue:
from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
list_display = ['nome', 'data_cadastro','ativo']
search_fields = ['nome']

admin.site.register(Produto, ProdutoAdmin)

#acesse o Django Admin via navegador (precisará usar o login e senha cadastrados quando o superusuário foi criado)
http://localhost:8000/admin

#listando os produtos cadastrados na home.html, primeiramente será necessário selecionar os produtos na view home, para isto edite core/views.py e altere a view home conforme o exemplo:
from .models import Produto

def home(request):
produtos_ativos = Produto.objects.filter(ativo=True)
return render(request, 'core/home.html', {'produtos': produtos_ativos})

#edite o core/templates/core/home.html adicionando o seguinte conteúdo
{% for produto in produtos %}
<p>{{ produto.data_cadastro|date:"d/m/Y h:i" }} - {{ produto.nome }}</p>
{% empty %}
<p>Nenhum cadastro de produto ativo no momento.</p>
{% endfor %}

#rode o projeto e acesse via navegador
python manage.py runserver

http://localhost:8000
```
## Dicas - Trabalhando com Querysets
> ***Mais detalhes na documentação oficial do Django:*** https://docs.djangoproject.com/en/1.11/ref/models/querysets/

```shell
#Levar em consideração os seguintes modelos:

class Entrega(models.Model):
mercadoria = models.CharField('Mercadoria', max_length=70)
endereco_cliente = models.CharField(u'Endereço', max_length=100)
data_cadastro = models.DateTimeField('Dt. cadastro',  auto_now_add=True)

def __unicode__(self):
return self.mercadoria


class Rastreamento(models.Model):
entrega = models.ForeignKey(Entrega)
data = models.DateTimeField('data cadastro', auto_now_add=True)
local = models.CharField('local', max_length=20)
ocorrencia = models.CharField(u'ocorrência', max_length=100)
origem = models.CharField('origem', max_length=20)
destino = models.CharField('destino', max_length=20)

def __unicode__(self):
return 'o: %s  d: %s' % (self.origem, self.destino)

#Buscar todas entregas cujo mercadoria contenha a string 'bola':
Entrega.objects.filter(mercadoria__icontains='bola')

#Buscar todas entregas de um determinado período:
Entrega.objects.filter(data__range=(data1, data2))
#Onde data1 e data2 são objetos do tipo Date ou DateTime

#Buscar todas entregas de um determinado período, exceto a que a mercadoria contenha a string 'bola':
Entrega.objects.filter(data__range=(data1, data2)).exclude(mercadoria__icontains='bola')
#Onde data1 e data2 são objetos do tipo Date ou DateTime

#Contar quantas entregas ocorreram no período:
Entrega.objects.filter(data__range=(data1, data2)).count()
#Retorna um inteiro

#Ordenar pela data da entrega:
Entrega.objects.all().order_by('data') #ordem ascendente
Entrega.objects.all().order_by('-data') #ordem descendente

#Retornar o primeiro ou o último objeto da queryset:
Entrega.objects.all().first()
Entrega.objects.all().last()

#Todos os rastreamentos de uma determinada entrega:
Rastreamento.objects.filter(entrega=obj_entrega)
#Onde obj_entrega é um objeto da classe Entrega

#Buscar um objeto pela chave primária 10
Rastreamento.objects.get(id=10)
Rastreamento.objects.get(pk=10)
#Retorna um objeto da classe Rastreamento

#Todos os rastreamentos onde a origem foi Santa Maria e que a mercadoria contenha a string 'bola':
Rastreamento.objects.filter(origem__contains='Santa Maria', entrega__mercadoria__icontains='bola')

#Buscar todos rastreamentos que passaram por cidades onde o nome inicia com a palavra “Santa”
from django.db.models import Q
Rastreamento.objects.filter(Q(origem__startwith = 'Santa') | Q(destino__startwith = 'Santa'))
#Retorna um objeto da classe Rastreamento
```
