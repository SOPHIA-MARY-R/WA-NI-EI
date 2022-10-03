from django.urls import URLPattern, path
from . import views

urlpatterns = [
   #path('',views.history),
   path('upload', views.upload_file, name='upload_file'),
]