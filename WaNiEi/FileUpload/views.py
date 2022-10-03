from dataclasses import dataclass
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from FileUpload.models import File
from .forms import UploadFileForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

def upload_file(request):
    if request.method=='POST':
        if request.FILES.getlist('FILE'):
            for f in request.FILES.getlist('FILE'):
                File(file=f).save()
            return render(request, 'FileUpload/upload.html')
        else:
           return HttpResponse('Upload unsuccessful!') 
           #return redirect(request, 'FileUpload/translate')
    else:
         return render(request, 'FileUpload/upload.html')

