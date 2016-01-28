from django.conf.urls import url, include
from rest_framework import routers
from shopomania_ck.orders import views as order_views

router = routers.DefaultRouter()
router.register(r'orders', order_views.OrderViewset, base_name='orders')
router.register(r'items', order_views.ItemViewset, base_name='items')
router.register(r'customers', order_views.CustomerViewset, base_name='customers')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^upload/$', order_views.FileUploadView.as_view()),
]
