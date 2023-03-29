from django.shortcuts import render
from usuarios.forms import loginForms, cadastroForms

def login(request):   
    form = loginForms()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):   
    form = cadastroForms()
    return render(request, 'usuarios/cadastro.html', {"form": form})