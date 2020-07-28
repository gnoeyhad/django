from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('', myapp.views.index, name='index'),
    path('blog/', myapp.views.blog, name='blog'),
    path('blog/<int:blog_id>', myapp.views.detail, name='detail'),
    path('blog/new/', myapp.views.new, name='new'),
    path('create/', myapp.views.create, name='create'),
    path('blog/<int:blog_id>/edit', myapp.views.edit, name='edit'),
    path('blog/<int:blog_id>/update', myapp.views.update, name='update'),
    path('blog/<int:blog_id>/delete', myapp.views.delete, name='delete'),
]
