from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3  # Количество объектов на одной странице
    page_query_param = 'page'  # Параметр запроса, указывающий номер страницы
    page_size_query_param = 'page_size'  # Параметр запроса, указывающий размер страницы
    max_page_size = 1000  # Максимальный размер страницы