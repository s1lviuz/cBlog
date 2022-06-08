from django import forms
from django.contrib.auth import forms as auth_forms

from .models import User

#User Forms

class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username",)

    def check(self):

        nome = self.data['first_name']

        if nome == '':
            return 'Este campo é obrigatório.'     
        pass


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username",)

class UserLogInForm(forms.Form):
    username = forms.CharField(required=True, label='Nome de Usuário')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Senha')

    
    def check(self):

        usuario = self.data['username']
        senha = self.data['password']

        #Checando Campos Vazios
        if usuario == '':
            str = 'Nome de Usuário'
            if senha == '':
                str += ' e Senha'
            return str + ' em branco'
        if senha == '':
            str = 'Senha'
            return str + ' em branco'


        #Checando se Usuário está cadastrado
        try:
            existe = User.objects.get(username=usuario)
        except:
            return 'Usuário não encontrado'
        
        return 0
        

        

        

    
    
    

