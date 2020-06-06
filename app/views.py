"""
Definition of views.
"""
from django.db import models
from django.shortcuts import render
from app import forms
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import AnketaForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import BlogForm
from django.shortcuts import render_to_response
from django.template import RequestContext



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    last_pages = Blog.objects.order_by("-id")[0:5]

    return render(
        request,
        'app/index.html',
        {
            'title':'GamesLife',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'last_pages': last_pages,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1':'Мужчина', '2': 'Женщина'}
    like = {'1':'Да', '2':'В целом да', '3':'Требует доработки',
           '4':'Если бы не эта форма...'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data.save()
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['gender'] = form.cleaned_data['gender']
            data['like'] = form.cleaned_data['like']
            data['news'] = form.cleaned_data['news']
            data['messege'] = form.cleaned_data['messege']
            data['email'] = form.cleaned_data['email']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/contact.html',
        {
            'title':'Отзывы',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'form':form,
            'data':data,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def video(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/video.html',
        {
            'title':'Video',
            'message':'Video',
            'year':datetime.now().year,
        }
    )


def gallery(request):
    """Renders the about page."""
    if request.method == "POST":
        blogform = BlogForm(request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.niw()
            blog_f.save()
            return redirect('page')
    else:
        blogform = BlogForm()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/gallery.html',
        {
            'title':'Создать статью',
            'blogform':blogform,
            'year':datetime.now().year,
        }
    )


def registration(request):

      regform = UserCreationForm (request.POST)
      if regform.is_valid(): #валидация полей формы

           reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы

           reg_f.is_staff = False # запрещен вход в административный раздел

           reg_f.is_active = True # активный пользователь

           reg_f.is_superuser = False # не является суперпользователем

           reg_f.date_joined = datetime.now() # дата регистрации

           reg_f.last_login = datetime.now() # дата последней авторизации

           reg_f.save() # сохраняем изменения после добавления данных

           messages.success(request,  'Account created successfully')

           return redirect('home') # переадресация на главную страницу после регистрации

      else:
          regform = UserCreationForm() 
      assert isinstance(request, HttpRequest)
      return render(
         request,

         'app/registration.html',
         {
           'regform': regform, # передача формы в шаблон веб-страницы
           'year':datetime.now().year,
         }
         )

def page(request):

    """Renders the blog page."""

    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели

    return render(

      request,

      'app/page.html',

            {

            'title':'Блог',

            'posts': posts, # передача списка статей в шаблон веб-страницы

            'year':datetime.now().year,

            }

            )

def blogpost(request, parametr):

     """Renders the blogpost page."""

     assert isinstance(request, HttpRequest)

     post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
     comments = Comment.objects.filter(post=parametr)  # запрос на выбор всех комментариев
     form = CommentForm(request.POST or None )
     if request.method == "POST":
         
         if form.is_valid():
             connect_f = form.save(commit=False)
             connect_f.author = request.user
             connect_f.date = datetime.now()
             connect_f.post = Blog.objects.get(id = parametr)
             connect_f.save() # сохраняем изменения после добавления полей

             return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария

         else:

             form = CommentForm() # создание формы для ввода комментария
     return render(

     request,

     'app/blogpost.html',

     {

     'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
     'comments': comments,
     'form': form,
     'year':datetime.now().year,

     }

     )
