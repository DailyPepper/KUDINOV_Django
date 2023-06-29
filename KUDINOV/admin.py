from django.contrib import admin
from django.contrib.auth.models import User

from .models import Articles
from .models import Women
from .models import Zakaz
from .models import Review
from .models import Order
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('products',)
    fieldsets = (
        (None, {"fields": ['products']}),
        ("Контактная информация", {"fields": ['first_name', 'last_name', 'email', 'gender']}),
    )


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'size', 'quantity')
    search_fields = ('title',)
    list_filter = ('price', 'size')


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'size', 'quantity')
    search_fields = ('title',)
    list_filter = ('price', 'size')


@admin.register(Zakaz)
class ZakazAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', 'payment_status')
    search_fields = ('title',)
    list_filter = ('date', 'status')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'anons', 'date')
    search_fields = ('title',)
    list_filter = ('date',)


@admin.register(Order)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_text', 'date')
    search_fields = ('title', 'full_text')
    list_filter = ('date',)
