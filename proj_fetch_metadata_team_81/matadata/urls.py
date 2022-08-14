from django.urls import path
from . import views 


urlpatterns=[
    
    
     path('', views.meta, name='meta'),
    
 
    ]