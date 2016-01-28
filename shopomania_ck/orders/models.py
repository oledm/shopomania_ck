from django.db import models
from django.utils import timezone 

class Order(models.Model):
    date = models.DateTimeField('Дата заказа', default=timezone.now)
    description = models.CharField('Описание заказа', max_length=150, null=True)
    author = models.CharField('Составитель', max_length=50, null=True)
    comment = models.CharField('Комментарий', max_length=200, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return 'Заказ {}'.format(self.date)


class Customer(models.Model):
    fio = models.CharField('ФИО покупателя', max_length=100, unique=True)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return self.fio

class Item(models.Model):
    order = models.ForeignKey(Order)
    customer = models.ForeignKey(Customer)
    description = models.CharField('Описание товара', max_length=200)
    price = models.PositiveIntegerField('Цена товара')
    link = models.CharField('Ссылка на сайт с описанием товара', max_length=1024)
    comment = models.CharField('Комментарий', max_length=200, null=True)

    def __str__(self):
        return '{}. {}, {}'.format(self.order, self.description, self.price)
