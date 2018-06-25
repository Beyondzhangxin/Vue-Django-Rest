from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'add', views.add_num),
    url(r'mul', views.mul_num),
]

urlpatterns = format_suffix_patterns(urlpatterns)