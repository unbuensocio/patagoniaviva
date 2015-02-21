from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
# from noticia.models import Noticia, Categoria
# from django_pager.pager import paginate

# Create your views here.
def portada(request):
    # slider_noticia = Noticia.objects.filter(estado=1)[:3]
    # portada_noticia = Noticia.objects.filter(estado=1)[1:9]
    # aleatorio = Noticia.objects.filter(estado=1).order_by('?')[:6]
    # allcategoria = Categoria.objects.all() 
    return render_to_response('portada/portada.html', locals(), context_instance=RequestContext(request))