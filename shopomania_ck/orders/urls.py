from django.conf.urls import url, include
#from django.views.generic import TemplateView
from rest_framework import routers

from .views import OrderViewset, ItemViewset, CustomerViewset, FileUploadView

router = routers.DefaultRouter()
router.register(r'orders', OrderViewset, base_name='orders')
router.register(r'items', ItemViewset, base_name='items')
router.register(r'customers', CustomerViewset, base_name='customers')

urlpatterns = [ 
    url(r'api/', include(router.urls)),
    url(r'api/uploads/', FileUploadView.as_view()),
    #url('^$', TemplateView.as_view(template_name='main/main.html')),
]
