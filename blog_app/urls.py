from django.urls import path

from . import views

urlpatterns= [
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]