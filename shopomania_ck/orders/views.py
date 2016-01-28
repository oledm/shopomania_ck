from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
import os
from .serializers import OrderSerializer, ItemSerializer, CustomerSerializer
from .models import Order, Item, Customer

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, pk=None):
        items = Item.objects.filter(order=pk)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Command for upload testing:
# curl --form "fileupload=@aaa.jpg" http://127.0.0.1:8000/api/uploads/
class FileUploadView(APIView):
    parser_classes = (FormParser, MultiPartParser, )

    def post(self, request, format=None):
        file_obj = request.data
        up_file = request.FILES['fileupload']
        print('Получен файл ', up_file)
        #new_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, up_file.name)
        #with open(new_path, 'wb+') as dest:
        #    for chunk in up_file.chunks():
        #        dest.write(chunk)
        return Response(status=204)


def index(request):
    print('Main rendering')
    return render(request, 'main/main.html', {'home': reverse('main:index')})
