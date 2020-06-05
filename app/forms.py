"""
Definition of forms.
"""
from django.db import models
from .models import Comment
from .models import Blog
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import datetime #for checking renewal date range.

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label = 'Ваше имя', min_length=2, max_length=100)
    gender = forms.ChoiceField(label = 'Ваш пол',
                               choices=[('1','м'), ('2','ж')],
                               widget=forms.RadioSelect, initial=1)
    like = forms.ChoiceField(label='Нравится ли вам наш сайт?', 
                             choices=(
                                 ('1','Да'),
                                 ('2','В целом да'),
                                 ('3','Требует доработки'),
                                 ('4','Если бы не эта форма...')))
    messege = forms.CharField(label='Комметарий', 
                              widget=forms.Textarea(attrs={'rows': 10, 'cols': 12}))

    news = forms.BooleanField(label='Хотели бы вы получать новости на email?',
                              required=False)
    email = forms.EmailField(label = 'email', min_length=7)



class CommentForm (forms.ModelForm):
  class Meta:
    model = Comment # используемая модель
    fields = ('text',) # требуется заполнить только поле text
    labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'posted', 'author', 'image',)
        labels = {'title':"Заголовок", 'description':"Краткое содержание", 'content':"Содержание", 'posted': "Дата", 'author':"Автор" }


