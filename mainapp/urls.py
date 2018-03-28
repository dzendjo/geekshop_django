
from django.conf.urls import url
import mainapp.views as mainapp

urlpatterns = [
    url(r'^$', mainapp.products, name='index'),
    url(r'^(\d+)/$', mainapp.products, name='category'),
]

