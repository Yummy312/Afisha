"""Afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/show_list_movie/', views.show_movie_list),
    path('api/v1/show_list_director/', views.show_director_list),
    path('api/v1/show_list_review/', views.show_review_list),
    path('api/v1/show_detail_movie/<int:id>/', views.show_detail_movie),
    path('api/v1/show_detail_director/<int:id>/', views.show_detail_director),
    path('api/v1/show_detail_review/<int:id>/', views.show_detail_review),
]