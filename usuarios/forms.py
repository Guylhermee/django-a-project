from django import forms

class loginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva",
                "name": "nome_login",                
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
                "name": "password",
            }
        )
    )

class cadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome Completo",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Barbosa Silva",
                "name": "nome_cadastro",                
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaobarbosa@xpto.com",
                "name": "email",
            }
        )
    )
    senhaCadastro = forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
                "name": "password_c",
            }
        )
    )
    senhaRepeat = forms.CharField(
        label="Confirmação de senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha mais uma vez",
                "name": "password_repeat",
            }
        )
    )