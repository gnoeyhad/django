from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog


def index(req):
    return render(req, 'index.html')

#읽기

def blog(req):
    blogs = Blog.objects
    return render(req, 'blog.html', {'blogs' : blogs})

def detail(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'detail.html', {'blog' : blog})

#생성

def new(req):
    return render(req, 'new.html')

def create(req):
    if(req.method == 'POST'):
        blog = Blog()
        blog.title = req.POST['title']
        blog.body = req.POST['body']
        blog.save()
    return redirect('/blog/'+str(blog.id))

#수정

def edit(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'edit.html', {'blog': blog})

def update(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.title = req.POST['title']
    blog.body = req.POST['body']
    blog.save()
    return redirect('/blog/'+str(blog_id))
    
#삭제

def delete(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('/blog/')