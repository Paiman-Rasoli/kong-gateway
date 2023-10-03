from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def upload(request):

      data = {
        'message': 'Hello, world!',
        'status': 'success'
      }
      return JsonResponse(data)




def retrieve():
      pass