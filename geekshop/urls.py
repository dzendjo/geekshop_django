"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'^products/', include(('mainapp.urls', 'mainapp'), namespace='products')),
    re_path(r'^contact/$', mainapp.contact, name='contact'),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),

    re_path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

