from django.core import serializers
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse,JsonResponse

from .models import *

def powerstationNumber(request):
    data=PowerStation.objects.all()
    # data=serializers.serialize('json',)
    print(data.count())
    return JsonResponse({'data':data.count()})
