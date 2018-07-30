from django.conf.urls import url
from . import views

app_name = "system"
urlpatterns = [
    # url(r'^postTest1/$', views.postTest1),
    # url(r'^postTest2/$', views.postTest2),
    # url(r'^$',views.index,name='index'),
    # url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$',views.detail,name='detail'),
    url(r'test$', views.apiTest, ),
    url(r'powerStations', views.powerStations),

]
