from django.conf.urls import url
from .views import *

urlpatterns = [
    #URLS DE INCIO/CIERRE/PERMISOS
    url(r'^$', home, name="home"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^noAccess/$', noAccess, name="noAccess"),

    #URLS DEL ROL CLIENTE
    url(r'^home/visitorsList$', body_view, name="visitorsList"),
    url(r'^home/addVisitor$', resident_view, name="addVisitor"),
]