from blog_app.models import Comentario, Post
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User

from .models import Seguir


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["autor"]


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        exclude = ["autor", "post"]


class SeguirForm(forms.ModelForm):
    class Meta:
        model = Seguir
        exclude = ["user", "seguindo"]


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = False
        self.fields["first_name"].widget.attrs["required"] = True
        self.fields["last_name"].widget.attrs["required"] = True
