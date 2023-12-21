# gestion_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('docentes/', views.docentes, name='docentes'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('administrativos/', views.administrativos, name='administrativos'),
    path('directivos/', views.directivos, name='directivos'),
]