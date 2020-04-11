from django.shortcuts import render, HttpResponse
from django.views import View
from . import views
import os
import json

#Import AWS SDK for python Boto
import boto3
from botocore.exceptions import NoCredentialsError

#Create your views here.
class Index(View):
    def get(self,request):
        AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_KEY=os.environ.get('AWS_SECRET_KEY')
        S3_BUCKET=os.environ.get('S3_BUCKET')
        return render(request,"upload/index.html",{})

class SignS3(View):
    def get(self,request):
        S3_BUCKET = os.environ.get('S3_BUCKET')

        file_name = request.args.get('file_name')
        file_type = request.args.get('file_type')

        s3 = boto3.client('s3')

        presigned_post = s3.generate_presigned_post(
            Bucket = S3_BUCKET,
            Key = file_name,
            Fields = {"acl": "public-read", "Content-Type": file_type },
            Conditions = [
                {"acl": "public-read"},
                {"Content-Type": file_type},
            ],
            ExpiresIn=3600,
        )

        return json.dumps({
            'data': presigned_post,
            'url': 'https//%s.s3.amazonaws.com/%s' % (S3_BUCKET,file_name)
        })

class UploadResult(View):
    def post(self,request):
        description=request.POST['description']
        image-url=request.POST['image-url']
        return render(request,"upload/result.html",{"image-url":image-url, "description":description})
