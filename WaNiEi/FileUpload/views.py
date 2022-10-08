from dataclasses import dataclass
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from googletrans import Translator

from FileUpload.models import File

def upload_file(request):
    if request.method=='POST':
        if request.FILES['FILE']:
            myfile=request.FILES['FILE']
            #File(title=myfile.name, file=myfile, created_at=datetime.datetime.now(), file_of=request.user).save()
            objJ=File()
            objJ.title=myfile.name
            objJ.file=myfile
            objJ.created_at=datetime.datetime.now()
            objJ.file_of=request.user
            objJ.save()
            myfilepath='D:/INDIGILAB_WORKSHOP/WaNiEi/WaNiEi/Files/'+myfile.name
            mytranslatedfilepath='D:/INDIGILAB_WORKSHOP/WaNiEi/WaNiEi/Files/translated_'+myfile.name
            mytranslatedfile='translated_'+myfile.name
            japContent=''
            with open(myfilepath, 'r', encoding='utf-8') as f:
                for line in f: japContent+=line
            f.close()
            Lines=japContent.split(' ')
            t=open(mytranslatedfilepath, 'w')
            engContent=''
            for line in Lines:
                translator=Translator()
                translated=translator.translate(line).text
                engContent+=translated
                t.write(translated)
            t.close()
            objE=File()
            objE.title=mytranslatedfile
            objE.file=mytranslatedfile
            objE.created_at=datetime.datetime.now()
            objE.file_of=request.user
            objE.save()

            return render(request, 'FileUpload/download.html', {'objE':objE, 'objJ':objJ, 'japContent':japContent, 'engContent': engContent})
        else:
           return HttpResponse('Upload unsuccessful!') 
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

def profile(request):
    Len=File.objects.filter(file_of=request.user).count()
    return render(request, 'FileUpload/profile.html', {'Len': Len})