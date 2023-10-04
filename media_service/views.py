import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from media_service.models import MediaModel
import os
import io



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
            file_name = os.path.basename(file_path).split(".")[0]
            new_media = MediaModel(name=file_name)
            new_media.image.save(file_name, get_file_data(file_path))
            new_media.save()
            return JsonResponse({"status" : 200 , "imageURL" : new_media.image.url , "imageName" : file_name})
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
            return JsonResponse({"status" : 200 , "fileURL" : find.image.url})
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