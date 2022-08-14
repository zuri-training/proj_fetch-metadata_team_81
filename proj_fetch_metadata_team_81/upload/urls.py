from django.urls import path
from . import views 


urlpatterns=[
    
     path('', views.uploadview.as_view(), name='up'),
     path('upload/', views.upload, name='upload'),
     path('result/', views.result,name='result'),
     path('createpdf/', views.render_pdf_view,name='createpdf')
     ]