from __future__ import absolute_import, unicode_literals
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import add, mul
from rest_framework import generics
import json


@api_view(['GET'])
def add_num(request, format='json'):
    if request.method == 'GET':
        dict = request.query_params.dict()
        res = add.delay(int(dict['num1']), int(dict['num2']))
        return Response(data=json.loads('{"res":' + str(res.get()) + '}'), content_type='/json')


@api_view(['GET'])
def mul_num(request, format='json'):
    if request.method == 'GET':
        dict = request.query_params.dict()
        res = mul.delay(int(dict['num1']), int(dict['num2']))
        return Response(data=json.loads('{"res":' + str(res.get()) + '}'), content_type='/json')


##this is from jason branch