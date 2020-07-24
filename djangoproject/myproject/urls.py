"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name='index'),
    path('blog/', myapp.views.blog, name='blog'),
    path('blog/<int:blog_id>', myapp.views.detail, name='detail'),
    path('blog/new/', myapp.views.new, name='new'),
    path('create/', myapp.views.create, name='create'),
    path('blog/<int:blog_id>/edit', myapp.views.edit, name='edit'),
    path('blog/<int:blog_id>/update', myapp.views.update, name='update'),
    path('blog/<int:blog_id>/delete', myapp.views.delete, name='delete'),
]
