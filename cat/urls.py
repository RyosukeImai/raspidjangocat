from django.urls import path
from . import views
app_name = 'cat'

urlpatterns = [
    path('', views.index, name='index'),    # /cat/index
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('catlist/', views.index, name='catlist'),    # /cat/index
    ]

