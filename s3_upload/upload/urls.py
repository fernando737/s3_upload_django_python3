from django.urls import path
from . import views
#Create your views here 

app_name="upload"

urlpatterns = [
    path('',views.Index.as_view(), name="index"),
]
