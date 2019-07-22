
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


# 接口功能描述
# 1. 概率分布建模功能
#   1.1 边际概率分布
#   1.2 联合概率分布
#   1.3 条件概率分布
#   1.4 调用EM算法
#   1.5 调用MAP算法
# 2. 概率分布计算功能
#   2.1 计算给定点PDF值
#   2.2 计算给定的CDF值
#   2.3 计算分位数
#   2.4 计算分布间KLD值 
#   2.5 计算分布间RMSE
#   2.6 计算线性变换分布
from . import views

urlpatterns = [
    url(r'model/distribution/$', views.Distribution.as_view()), #跟据请求不同转发到不同的功能
    url(r'getAllDistributionConfigs', views.getAllDistributionConfigs),
    url(r'calculation',views.calculate),
    url(r'del',views.delModel),
    url(r'testGMM',views.test_gmm),
    url(r'gmm_qinghai',views.gmm_qinghai),
    url(r'^image$', views.my_image, name="image"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
