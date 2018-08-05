from django.core import serializers
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_http_methods

from .models import *

def powerstationNumber(request):
    data=PowerStation.objects.all()


    # data=serializers.serialize('json',)
    print(data.count())
    return JsonResponse({'data':data.count()})




@require_http_methods(['GET'])
def apiTest(request):
    response = {}
    try:
        books = PowerStation.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

