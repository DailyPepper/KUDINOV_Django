from django.contrib import admin
from django.core.mail import send_mail
from .models import Articles
from .models import Women
from .models import Zakaz
from .models import Review
from .models import Order
from .models import Customer
from import_export.admin import ImportExportModelAdmin
from .resources import ArticlesResource


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('products',)
    list_filter = ('gender',)
    fieldsets = (
        (None, {"fields": ['products']}),
        ("Контактная информация", {"fields": ['first_name', 'last_name', 'email', 'gender']}),
    )
    raw_id_fields = ('products',)
    actions = ['send_email']
    def send_email(self, request, queryset):
        for customer in queryset:
            send_mail(
                'Привет!',
                'Привет, {}'.format(customer.first_name),
                'admin@example.com',
                [customer.email],
                fail_silently=False,
            )
        self.message_user(request, 'Электронное письмо отправлено.')

    send_email.short_description = 'Отправить электронное письмо'


@admin.register(Articles)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'size', 'quantity')
    search_fields = ('title',)
    list_filter = ('size', 'price')
    resource_class = ArticlesResource

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            price = float(search_term)
            queryset |= self.model.objects.filter(price__gte=price)
        except ValueError:
            pass
        return queryset, use_distinct

# class ArticlesResource(resources.ModelResource):
#     class Meta:
#         model = Articles

@admin.register(Women)
class WomenAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price', 'size', 'quantity')
    search_fields = ('title',)
    list_filter = ('size', 'price')

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            price_from = float(search_term)
            price_to = float(search_term)
            if price_from:
                queryset |= self.model.objects.filter(price__gte=price_from)
            if price_to:
                queryset &= self.model.objects.filter(price__lte=price_to)
        except ValueError:
            pass
        return queryset, use_distinct

    def get_export_queryset(self, request):
        return Women.objects.all()

    def export_women_to_excel(request):
        queryset = request.get_export_queryset()
        return ExcelResponse(
            queryset,
            output_name='women_export',
            headers=['Название', 'Цена', 'Размер', 'Фото', 'Характеристика', 'Дата публикации', 'Количество']
        )


@admin.register(Zakaz)
class ZakazAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', 'payment_status')
    search_fields = ('title',)
    list_filter = ('date', 'status', 'payment_status')


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






