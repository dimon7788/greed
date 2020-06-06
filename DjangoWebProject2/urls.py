"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
import django.contrib.auth.views
from django.conf.urls import url
from django.conf.urls import *
import app.forms
import app.views
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^video$', app.views.video, name='video'),
    url(r'^page$', app.views.page, name='page'),     
    url(r'^gallery$', app.views.gallery, name='gallery'),    
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^registration$', app.views.registration, name='registration'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),





]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()