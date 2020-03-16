from django.contrib import admin
from django.conf.urls import url
from basicApp import views
from django.urls import path

#TEMPLATE TAGGING
app_name = 'basicApp'

urlpatterns = [
    #url(r'^userLogin/$',views.userLogin,name='userLogin'),
    path('userLogin/',views.userLogin,name='userLogin'),
    url(r'^registration/$',views.registration,name='registration'),
    path('special/',views.special,name='special'),
]
