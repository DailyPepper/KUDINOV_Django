from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kurs.views import CustomerAPIView
from kurs.views import ArticlesViewSet

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('my-view/', views.my_view, name='my_view'),
]
urlpatterns += staticfiles_urlpatterns()
