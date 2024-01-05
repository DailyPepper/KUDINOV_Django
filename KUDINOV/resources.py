from import_export import resources, fields
from KUDINOV.models import Articles

class ArticlesResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    title = fields.Field(column_name='Название', attribute='title')
    price = fields.Field(column_name='Цена', attribute='price')
    size = fields.Field(column_name='Размер', attribute='size')
    photo = fields.Field(column_name='Фото', attribute='photo')
    full_text = fields.Field(column_name='Полный текст', attribute='full_text')
    date = fields.Field(column_name='Дата', attribute='date')
    quantity = fields.Field(column_name='Количество', attribute='quantity')

    class Meta:
        model = Articles
        fields = ('id', 'title', 'price', 'size', 'photo', 'full_text', 'date', 'quantity')
        export_order = ('id', 'title', 'price', 'size', 'photo', 'full_text', 'date', 'quantity')
        batch_size = 100

    def dehydrate_price(self, article):
        return f"{article.price} руб"

    def get_queryset(self):
        return Articles.objects.order_by('id')

    def get_export_queryset(self, request=None, queryset=None):
        # You can customize the export queryset based on your needs
        return queryset
