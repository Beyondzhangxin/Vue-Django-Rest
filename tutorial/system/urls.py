from django.conf.urls import url
from . import views

app_name = "system"
urlpatterns = [
    # url(r'^postTest1/$', views.postTest1),
    # url(r'^postTest2/$', views.postTest2),
    # url(r'^$',views.index,name='index'),
    # url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$',views.detail,name='detail'),
    url(r'test$', views.apiTest),
    url(r'powerStations', views.powerStations),
    url(r'totalVolume',views.totalVolume),
    url(r'totalGeneratingCapacity_today',views.totalGeneratingCapacity_today),
    url(r'totalGeneratingCapacity_thisMonth',views.totalGeneratingCapacity_thisMonth),
    url(r'totalGeneratingCapacity',views.totalGeneratingCapacity),
    url(r'echartsDataForInverterFDL',views.echartsDataForInverterFDL),
    url(r'echartsDataForInverterFDGL',views.echartsDataForInverterFDGL),
    url(r'echartsDataForFZD',views.echartsDataForFZD),
    url(r'powerStationsNum',views.powerStationsNum),
    url(r'getStationMonitorInfo',views.getStationMonitorInfo),
    url(r'getDeviceMonitor',views.getDeviceMonitor),
    url(r'getDQFDGL',views.getDQFDGL),
    url(r'getDeviceTable',views.getDeviceTable),
    url(r'getHBSJ',views.getHBSJ),#获取环保数据
    url(r'getStationCompareInfo',views.getStationCompareInfo),#获取电站对比数据
    url(r'getDeviceCompareInfo',views.getDeviceCompareInfo),#获取设备对比数据
    url(r'getDetectionInfo',views.getDetectionInfo),#获取故障检测数据
    url(r'getAllSystems',views.getAllSystems),#获取所有系统的列表
    url(r'getAllParamsBySystemType',views.getAllParamsBySystemType),#获取某个系统对应的所有变量列表

]
