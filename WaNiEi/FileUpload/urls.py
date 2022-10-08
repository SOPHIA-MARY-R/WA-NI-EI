
from django.urls import URLPattern, path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('profile/', views.profile, name='profile'),
   path('upload/', views.upload_file, name='upload'),
   path('history/', views.history, name='history'),
   path('delete/<int:id>', views.delete, name='delete'),
] 