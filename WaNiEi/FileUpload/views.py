from dataclasses import dataclass
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from FileUpload.models import File
from .forms import UploadFileForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

def upload_multiple_files(request):
    if request.method=='POST':
        if request.FILES.getlist("files"):
            saverecord=File()
            myfiles = request.FILES.getlist("files")
            for f in myfiles:
                saverecord.file=f
                #saverecord.file_of=request.User
                saverecord.save()
            return render(request, 'FileUpload/upload.html')
        else:
           return HttpResponse('Upload unsuccessful!') 
           #return redirect(request, 'FileUpload/translate')
    else:
         return render(request, 'FileUpload/upload.html')

