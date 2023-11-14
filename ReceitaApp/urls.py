from django.urls import path
from ReceitaApp import views


urlpatterns = [ 
    path('', views.index, name='index'),
    path('receitas/', views.receitas, name='receitas'),
    path('receita/<int:id>', views.detalhes_receita, name='receita')
]