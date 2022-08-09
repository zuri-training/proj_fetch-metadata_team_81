from django.contrib.sites import requests
from django.core.files.storage import FileSystemStorage
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import fileUpload
from django.views import generic
from django.urls import reverse_lazy
from datetime import datetime
# Create your views here.

class uploadview(generic.ListView):
    model=fileUpload
    context_object_name="files"
    template_name='registration/dashboard.html'
    paginate_by=10
   
    def get_queryset(self):
        return fileUpload.objects.order_by('id') 

#def simple_upload(request):
#    if request.method == 'POST' and request.FILES['myfile']:
#        myfile = request.FILES['myfile']
#        fs = FileSystemStorage()
#        filename = fs.save(myfile.name, myfile)
#        uploaded_file_url = fs.url(filename)
#        return render(request, 'core/simple_upload.html', {
#            'uploaded_file_url': uploaded_file_url
#        })
#    return render(request, 'core/simple_upload.html')


def upload(request):
    if request.method== 'POST':
        myfile=request.FILES['myfile']
        date_uploaded= datetime.now()
      
        #if myfile.endwith('png'):
        #    filename="png"
        a=fileUpload(myfile=myfile, date_uploaded=date_uploaded)
        a.save()
        #messages.success(request, "Successful file submission")
        return redirect('up')
    else:
        return redirect('up')

def meta(request):
    #fileurl=request.POST['name']
    mean=request.POST.get('mename')
    print(mean)

    return redirect('up')



