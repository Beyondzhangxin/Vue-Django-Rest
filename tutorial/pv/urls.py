
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
# (1)一个为分页查询
# (2)根据年求和
# (3)根据月求和
# (4)根据日求和


urlpatterns = [
    # 得到总和
    url(r'get/$', views.PvdataList.as_view()),
    url(r'get/(?P<year>.{4})/$', views.PvdataSumYear.as_view()),
    url(r'get/(?P<year>.{4})/(?P<month>.{1,2})/$', views.PvdataSumMonth.as_view()),
    url(r'get/(?P<year>.{4})/(?P<month>.{1,2})/(?P<day>.{1,2})/$', views.PvdataSumDay.as_view()),
    url(r'get/(?P<year>.{4})/(?P<month>.{1,2})/(?P<day>.{1,2})/lte/$', views.PvdataSumDayLte.as_view()),
    # 得到某台数的一天的
    url(r"get/detection/(?P<year>.{4})/(?P<month>.{1,2})/(?P<day>.{1,2})/", views.DetectionList.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
