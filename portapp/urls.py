from django.urls import path
from portapp import views


urlpatterns = [
    path('',views.home,name='index.html'),
    path('download_file',views.download_file,name='download_file'),


]