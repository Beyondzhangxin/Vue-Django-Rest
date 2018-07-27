import json
import time
from datetime import date
from datetime import datetime
from .models import Pvdata
from .serializer import PvdataSerializer, PvDataDetectionList
from django.db.models import Sum, Count, Avg, Min, Max
# Create your views here.
from rest_framework import generics
from rest_framework import pagination
from django.db.models import FloatField
from rest_framework.response import Response
from django.core import serializers


# 序列化
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# 分页类的设置
class PvdataPagination(pagination.PageNumberPagination):
    """
    配置分页规则
    """
    page_size = 2
    page__size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# 基于类的视图
class PvdataList(generics.ListCreateAPIView):
    queryset = Pvdata.objects.all()
    serializer_class = PvdataSerializer
    pagination_class = PvdataPagination

    def get(self, request, *args, **kwargs):
        try:
            self.pagination_class.page_size = request.query_params.dict()['page_size']
        except KeyError:
            return self.list(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


# 对年月日搜索
class PvdataSumYear(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        if self.queryset == 0:
            return Response(json.loads('{"error":"没有找到对应的时间"}'), content_type='/json')
        j = 5 * self.queryset.aggregate(Sum('p')).get('p__sum')/1000/3600
        data = json.loads('{"j":' + str(j) + '}')
        print(data)
        return Response(data)

    def get_queryset(self):
        return Pvdata.objects.filter(updatetime__year=self.kwargs.get('year'))


class PvdataSumMonth(PvdataSumYear):
    def get_queryset(self):
        return Pvdata.objects.filter(updatetime__year=self.kwargs.get('year'),
                                     updatetime__month=self.kwargs.get('month'))


class PvdataSumDay(PvdataSumMonth):

    def get_queryset(self):
        return Pvdata.objects.filter(updatetime__year=self.kwargs.get('year'),
                                     updatetime__month=self.kwargs.get('month'),
                                     updatetime__day=self.kwargs.get('day'))


class PvdataSumDayLte(PvdataSumYear):
    def get_queryset(self):
        year = int(self.kwargs.get('year'))
        month = int(self.kwargs.get('month'))
        day = int(self.kwargs.get('day'))
        return Pvdata.objects.filter(updatetime__date__lte=date(year=year, month=month, day=day))


class DetectionPagination(pagination.PageNumberPagination):
    page_size = 1
    page__size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class DetectionList(generics.ListAPIView):
    queryset = Pvdata.objects.all()
    serializer_class = PvDataDetectionList
    pagination_class = DetectionPagination

    """
        List a queryset.
        """

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        queryset = self.filter_queryset(query)
        page = self.paginate_queryset(queryset)

        if page is not None:
            # serializer = self.get_serializer(page, many=True)
            # return self.get_paginated_response(serializer.data)
            # 个性序列化
            serializer = json.dumps(page, cls=CJsonEncoder)
            return self.get_paginated_response(json.loads(serializer))
        serializer = json.dumps(page, cls=CJsonEncoder)
        return Response(serializer.data)

    def get_queryset(self):
        year = int(self.kwargs.get('year'))
        month = int(self.kwargs.get('month'))
        day = int(self.kwargs.get('day'))
        return Pvdata.objects.filter(updatetime__date=date(year=year, month=month, day=day))\
            .values('pcbid', 'cityid').annotate(p_avg=Avg('p'), time_sum=Count('updatetime')
            /Count('channelid', distinct=True), time_min=Min('updatetime'), time_max=Max('updatetime'))
    # def get_time(self, queryset):
    #     queryset.aggregate()

