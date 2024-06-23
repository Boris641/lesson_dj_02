from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name='home'),
    path('new', views.new, name='page_1'),
    path('opinions', views.opinions, name='page_2'),
    path('contacts', views.contacts, name='last')

]