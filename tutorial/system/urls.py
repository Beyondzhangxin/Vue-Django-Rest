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
    url(r'getDeviceMonitor',views.getDeviceMonitor)


]
