from pathlib import Path
from django.contrib.sites import requests
from django.core.files.storage import FileSystemStorage
from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import fileUpload
from django.views import generic
from django.urls import reverse_lazy
from datetime import datetime
from pprint import pprint
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from django.utils.encoding import smart_str
from .outterfunc.extractImage import extract_image_metadata
from .outterfunc.extractPdf import extract_pdf_file
from .outterfunc.defaultMetadata import default_metadata
from django.utils.datastructures import MultiValueDictKeyError
from django.conf import settings
from django.core.files import File
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  


# Create your views here.


   

def handle_uploaded_file(f):
    with open('metadata / upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload(request):
    if request.method== 'POST':
        filetype='video'
        uploaded_file=''
        try:
                myfile = request.FILES['myfile']
        except MultiValueDictKeyError:
                myfile = False
        if myfile:
            #if 'myfile' in request.POST:
            
            
            #else:
                
       
            date_uploaded= datetime.now()
            


      
            #if myfile.endwith('png'):
            #    filename="png"
            a=fileUpload(myfile=myfile, date_uploaded=date_uploaded)
            a.save()
            context = {"metadata": []}
            uploaded_file = myfile
            file_type = uploaded_file.content_type.split("/")
            filetype=file_type[0]
        if not myfile:
            return redirect('up')
            #mean=request.POST.get('mename')
            #path = Path(mean[1:])
            #myfile = fileUpload.objects.get(filename='user.png')
            #with path.open(mode='rb') as f:
            #    myfile.myfile = File(f)
            #    myfile.save()
            #
            #    if 'video' in mean:
            #        filetype="video"
            #    if 'image' in mean:
            #        filetype="image"
            #    if 'audio' in mean:
             #       filetype="audio"
        if filetype == "video" or filetype == "image" or filetype == "audio":

            extracted_metadata = extract_image_metadata(
                filetype, uploaded_file)
            context['metadata'] += extracted_metadata

        elif  "pdf" in file_type:
                pdf = extract_pdf_file(uploaded_file)
                context['metadata'] += pdf

        else:
            context['metadata'] += default_metadata(uploaded_file)

        request.session["metadata"] = context

        if uploaded_file.size < 20000000:
            name = uploaded_file.name
            #owner = request.user
            #filee = fileUpload.objects.filter(filename=name).exists()

            #if not filee:
            data = fileUpload(filename=name,filetype=filetype,metadata=context)
            data.save()

            #return redirect("result")
        #messages.success(request, "Successful file submission")
        return redirect('up')
        #return render(request,'registration/index (2).html',context)
        
    else:
        return render(request,'registration/index.html')

class uploadview(generic.ListView):
    model=fileUpload
    context_object_name="files"
    
    template_name='registration/index (2).html'
    paginate_by=15
    
    
   
    
    #def get_context_data(self, **kwargs):
    #    context=super(uploadview, self).get_context_data(**kwargs)
    #    self.object_list = self.get_context_data()
    #    metadata = self.request.session.get("metadata")
    #    context = metadata
    #    context['query']=fileUpload.objects.order_by('id')
    #    print(metadata)
    #    return context

    def get_queryset(self):
        #context=super(uploadview, self).get_context_data(**kwargs)
        #metadata = self.request.session.get("metadata")
        #if context is None:
        #    print(context)
        #context = metadata

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


def result(request):
    metadata = request.session.get("metadata")
    context = metadata
    print(metadata)

    return render(request,'registration/metadata.html',context)

def render_pdf_view(request):
    metadata = request.session.get("metadata")
    template_path = 'registration/metadata.html'
    context = metadata
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

