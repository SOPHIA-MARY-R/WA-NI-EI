from dataclasses import dataclass
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from googletrans import Translator

from FileUpload.models import File
#from .forms import UploadFileForm
#from django.views.generic.edit import CreateView
#from django.views.generic.edit import FormView

def upload_file(request):
    if request.method=='POST':
        if request.FILES['FILE']:
            myfile=request.FILES['FILE']
            File(title=myfile.name, file=myfile, created_at=datetime.datetime.now(), file_of=request.user).save()
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
            obj=File()
            obj.title=mytranslatedfile
            obj.file=mytranslatedfile
            obj.created_at=datetime.datetime.now()
            obj.file_of=request.user
            obj.save()
            #File(title=mytranslatedfile, file=mytranslatedfile, created_at=datetime.datetime.now()).save()
            return render(request, 'FileUpload/download.html', {'object':obj})
        else:
           return HttpResponse('Upload unsuccessful!') 
           #return redirect(request, 'FileUpload/translate')
    else:
         return render(request, 'FileUpload/upload.html')

def home(request):
    return render(request, 'fileupload/home.html')

def history(request):
    FilesList=File.objects.filter(file_of=request.user)
    return render(request, 'FileUpload/history.html', {'FilesList':FilesList})

def delete(request, id):
    FileList = File.objects.get(id=id)
    FileList.delete()
    return redirect('/fileupload/history')