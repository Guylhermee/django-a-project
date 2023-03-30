from django.shortcuts import render,redirect
from usuarios.forms import loginForms, cadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):   
    form = loginForms()
    if request.method == 'POST':
        form = loginForms(request.POST)
        if form.is_valid:
            nome=form["nome_login"].value()
            senha=form["senha"].value()

        usuario = auth.authenticate(
            request, 
            username=nome, 
            password=senha 
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso!")
            return redirect('index') 
        else:
            messages.error(request, "Erro ao tentar logar!")
            return redirect('login') 

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):   
    form = cadastroForms()
    if request.method == 'POST':
        form = cadastroForms(request.POST)
        if form.is_valid:
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senhaCadastro"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Esse usuário já existe!")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')