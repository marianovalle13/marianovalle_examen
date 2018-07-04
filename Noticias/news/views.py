from django.shortcuts import render
from .models import *
from Noticias.urls import *
# Create your views here.

def obtener_Noticias(request):
    obtener_noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {"noticias": obtener_noticias})

def añadir_Comentario(request, noticia_id):
    comentario = Comentario(noticia=Noticia.objects.get(id=noticia_id), comentario=request.POST['comentario'])
    comentario.save()
    if comentario: return redirect("añadir_noticias")
    else: return HttpResponse("Error")
