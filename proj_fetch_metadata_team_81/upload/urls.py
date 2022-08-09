from django.urls import path
from . import views 


urlpatterns=[
    
     path('', views.uploadview.as_view(), name='up'),
     path('upload/', views.upload, name='upload'),
     path('meta/', views.meta, name='meta'),
   
     ]