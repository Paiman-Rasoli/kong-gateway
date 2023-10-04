'''
Note: In this assessment I focused on Kong and File manipulation. not so much on Django code style! 
'''
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from media_service.models import MediaModel
import os
import io
import uuid



@csrf_exempt
@require_POST
def upload(request):
      try:
            body = request.body.decode('utf-8') 
            json_data = json.loads(body)
            file_path = json_data.get('file_path')
      except Exception as e:
            return JsonResponse({"message" : "file_path is required" , "status" : 400})

      if isExist(file_path):
            file_name = str(uuid.uuid4())
            new_media = MediaModel(name=file_name)
            new_media.image.save(file_name, get_file_data(file_path))
            new_media.save()
            response = {
              "status" : 200,
              "imageURL" : new_media.image.url,
              "imageName" : file_name
            }
            return JsonResponse(response)
      else:
            error = {
                  "status" : 400,
                  "message" : "File not exist."
            }
            return JsonResponse(error)

def retrieve(request):
      file_name = request.GET.get("file_name")
      if file_name == None:
            return JsonResponse({"status" : 400 , "message" : "File Name is required"})
      try:
            find = MediaModel.objects.get(name=file_name)
            response = {
                  "status" : 200 ,
                  "fileURL" : find.image.url
            }
            return JsonResponse(response)
      except Exception as e:
            print(e)
            return JsonResponse({"status" : 404 , "message" : "image not found"})



# utils
def isExist(file_path : str) -> bool:
      return os.path.exists(file_path)


def get_file_data(file_path : str):
    with open(file_path, 'rb') as file:
        image_file = io.BytesIO(file.read())
    return image_file