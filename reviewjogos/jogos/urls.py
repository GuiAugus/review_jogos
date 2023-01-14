from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jogos/', views.JogosListView.as_view(), name='jogos'),
    path('jogos/<int:pk>', views.JogoDetailView.as_view(), name='jogo-detail')
]  