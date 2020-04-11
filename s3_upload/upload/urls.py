from django.urls import path
from . import views
#Create your views here 

app_name="upload"

urlpatterns = [
    path('',views.Index.as_view(), name="index"),
    path('sign_s3', views.SignS3.as_view(), name="sign_s3"),
    path('upload_result', views.UploadResult.as_view(),name="upload_result"),
]
