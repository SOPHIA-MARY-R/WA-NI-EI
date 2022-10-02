from django.urls import URLPattern, path
from . import views

urlpatterns = [
   #path('',views.history),
   path('upload', views.upload_multiple_files, name='upload_multiple_files'),
]