from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path('equipos/', views.EquipoList.as_view(), name='equipos'),
    path('equipos/<int:pk>/', views.EquipoDetail.as_view()),
    path('jugadores/', views.JugadorList.as_view()),
    path('jugadores/<int:pk>/', views.JugadorDetail.as_view()),
]
