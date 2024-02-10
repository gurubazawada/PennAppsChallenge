from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('application/', views.application, name = 'application'),
    path('', include("django.contrib.auth.urls")),
    path('logout', views.logout),
    path("signup/", views.signup, name='signup'),
    path('submit-application', views.application),
    path('createUser', views.createUser),

]
