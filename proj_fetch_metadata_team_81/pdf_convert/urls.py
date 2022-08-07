from django.urls import path

from . import views

urlpatterns = [
    path('render/pdf/', Pdf.as_view())
]
