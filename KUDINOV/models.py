from django.db import models
from django.contrib import admin


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0.0)
    size = models.CharField(max_length=10)
    photo = models.ImageField('Фото', upload_to='products/', default='')
    full_text = models.TextField('Характеристика')
    date = models.DateTimeField('Дата публикации')
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'М-товар'
        verbose_name_plural = 'Мужсукие товары'


class Women(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0.00)
    size = models.CharField(max_length=10, default='')
    photo = models.ImageField('Фото', upload_to='products/', default='')
    full_text = models.TextField('Характеристика')
    date = models.DateTimeField('Дата публикации')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ж-товар'
        verbose_name_plural = 'Женские товары'


from django.db import models


class Zakaz(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    status = models.CharField('Статус', max_length=50)
    payment_status = models.CharField('Статус оплаты', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    @classmethod
    def get_all_orders(cls):
        return cls.objects.all()

    @classmethod
    def filter_orders(cls, status=None, payment_status=None):
        queryset = cls.objects.all()

        if status:
            queryset = queryset.filter(status=status)
        if payment_status:
            queryset = queryset.filter(payment_status=payment_status)

        return queryset

    def update_order_status(self, new_status):
        self.status = new_status
        self.save()

    def set_payment_status(self, new_payment_status):
        self.payment_status = new_payment_status
        self.save()

    @classmethod
    def create_order(cls, title, anons, full_text, date, status, payment_status):
        order = cls(title=title, anons=anons, full_text=full_text, date=date, status=status,
                    payment_status=payment_status)
        order.save()
        return order

    def delete_order(self):
        self.delete()


class Review(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Order(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Отзыв')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о товаре'
        verbose_name_plural = 'Информация о товарах'


class Product(models.Model):
    name = models.CharField(max_length=50)


class Customer(models.Model):
    first_name = models.CharField('Имя', max_length=50, default='')
    last_name = models.CharField('Фамилия', max_length=50, default='')
    email = models.EmailField('Электронная почта', default='')
    gender_choices = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    )
    gender = models.CharField('Пол', max_length=1, choices=gender_choices, default='')
    products = models.ManyToManyField(Order)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
