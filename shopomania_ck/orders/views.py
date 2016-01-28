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
from shopomania_ck.xlimport.helpers import ExcelImporter

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
# curl --form "fileupload=@data.xls" http://127.0.0.1:8000/api/uploads/
class FileUploadView(APIView):
    parser_classes = (FormParser, MultiPartParser, )

    def post(self, request, format=None):
        file_obj = request.data
        up_file = request.FILES['fileupload']
        print('Received file', up_file)
        self.procFile(up_file)
        return Response(status=204)

    def procFile(self, fname):
        saved_file = os.path.join(settings.MEDIA_ROOT, fname.name)
        with open(saved_file, 'wb+') as dest:
            for chunk in fname.chunks():
                dest.write(chunk)

        self.parseExcel(saved_file)

    def parseExcel(self, fname):
        excel_importer = ExcelImporter()
        header, data =  excel_importer.read(fname)
        print('Data export success: ', data)
        self.createNewOrder(data)

    def createNewOrder(self, data):
        order = Order.objects.create()
        for order_id, customer, item, price, link in data:
            customer_, created = Customer.objects.get_or_create(fio=customer)
            if not created:
                customer_.save()
            Item.objects.create(description=item, price=price, link=link,
                                customer_id=customer_.id, order_id=order.id)


def index(request):
    print('Main rendering')
    return render(request, 'main/main.html', {'home': reverse('main:index')})
