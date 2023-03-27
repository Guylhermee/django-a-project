from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
# Create your views here. 

def index(request):   
    fotografias = Fotografia.objects.order_by("-date").filter(publicada=True)  #lista de objetos criados no banco
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id): 
    fotografia = get_object_or_404(Fotografia, pk=foto_id)               
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia })

def buscar(request): 
    fotografias = Fotografia.objects.order_by("-date").filter(publicada=True)  #lista de objetos criados no banco

    if "buscar" in request.GET:         #se tem "buscar" na url
        nome_a_buscar = request.GET['buscar']   
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) #icontains busca parte do texto


    return render(request, "galeria/buscar.html", {"cards": fotografias})