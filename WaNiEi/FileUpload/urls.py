from django.conf import settings
from django.conf.urls.static import static
from django.urls import URLPattern, path
from . import views

urlpatterns = [
   #path('',views.history),
   path('upload', views.upload_file, name='upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)