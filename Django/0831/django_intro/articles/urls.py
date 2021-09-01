from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    path('index/', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('read/<str:username>/', views.read, name = 'read'),
]
