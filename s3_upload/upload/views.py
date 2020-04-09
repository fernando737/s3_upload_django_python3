from django.shortcuts import render, HttpResponse
from django.views import View
from . import views

#Import AWS SDK for python Boto
import boto3
from botocore.exceptions import NoCredentialsError

#Create your views here.
class Index(View):
    def get(self,request):
        return render(request,"upload/index.html",{})
    def post(self, request):
        return render(request,"upload/index.html",{})

