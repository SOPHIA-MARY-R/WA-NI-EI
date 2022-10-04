from dataclasses import dataclass
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from googletrans import Translator

from FileUpload.models import File
#from .forms import UploadFileForm
#from django.views.generic.edit import CreateView
#from django.views.generic.edit import FormView

def upload_file(request):
    if request.method=='POST':
        if request.FILES['FILE']:
            myfile=request.FILES['FILE']
            File(title=myfile.name, file=myfile, created_at=datetime.datetime.now()).save()
            myfilepath='D:/INDIGILAB_WORKSHOP/WaNiEi/WaNiEi/Files/'+myfile.name
            mytranslatedfilepath='D:/INDIGILAB_WORKSHOP/WaNiEi/WaNiEi/Files/translated_'+myfile.name
            mytranslatedfile='translated_'+myfile.name
            string=''
            with open(myfilepath, 'r', encoding='utf-8') as f:
                for line in f: string+=line
            f.close()
            Lines=string.split(' ')
            t=open(mytranslatedfilepath, 'w')
            for line in Lines:
                translator=Translator()
                translated=translator.translate(line).text
                t.write(translated)
            t.close()
            File(title=mytranslatedfile, file=mytranslatedfile, created_at=datetime.datetime.now()).save()
            return render(request, 'FileUpload/upload.html')
        else:
           return HttpResponse('Upload unsuccessful!') 
           #return redirect(request, 'FileUpload/translate')
    else:
         return render(request, 'FileUpload/upload.html')