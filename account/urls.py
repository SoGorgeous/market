# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from shop import views as view
urlpatterns=[
        #django_login/django_logut urls
        url(r'login/$','django.contrib.auth.views.login',name='login'),
        url(r'logout/$',views.logout,name='logout'),
        
        #Chnange password urls
        url(r'password-change/$','django.contrib.auth.views.password_change',name='password_change'),
        url(r'password-change-done/$','django.contrib.auth.views.password_change_done',name='password_change_done'),
          
        # restore password urls
        url(r'^password-reset/$','django.contrib.auth.views.password_reset',name='password_reset'),
        url(r'^password-reset/done/$','django.contrib.auth.views.password_reset_done',name='password_reset_done'),
       
        url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$','django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
        url(r'^password-reset/complete/$','django.contrib.auth.views.password_reset_complete',name='password_reset_complete'),
        
        #register an account
        url(r'^register/$', views.register, name='register'),
        
        url(r'^$',views.homepage,name='homepage'),
        
        url(r'^edit/$',views.edit,name='edit'),
        
        url(r'^list/$',view.product_list,name='product_list'),
        ]
