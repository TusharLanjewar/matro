"""matro URL Configuration

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
from django.urls import path,include
from website.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage),
    path('about/',about),
    path('search/',search),
    path('membership/',membership),
    path('contact/',contact),
    path('happystories/',happystories),
    path('faq/',faq),
    path('shortaa/<int:id>',shortaa,name='shortaa'),
    path('terms/',terms),
    path('privacy/',privacy),
    path('disclaimer/',disclaimer),
    path('serchdetail/',serchdetail),
    path('searchdetail/',searchdetail),
    path('g/',g),
    path('apply',apply,name='apply'),
    path('slists',slists,name='slists'),
    path('blogss/',blogss),
    path('apply1',apply1,name='apply1'),
    path('blogdetail/<int:id>',blogdetail),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login1/',LoginView.as_view(),name='login1'),
    path('logout1/',LogoutView.as_view(),name='logout1'),
    path('log/',log),
    path('happystory/',happystory),
    path('stories/<int:id>',stories),
    path('register/',register),
    path('insertregister/',insertregister),
    path('paytm/',include('paytm.urls'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
