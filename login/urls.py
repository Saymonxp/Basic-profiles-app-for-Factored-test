from django.urls import path
from . import views

#URL configuration
urlpatterns = [
    path('login/', views.render_login, name='render_login')
]