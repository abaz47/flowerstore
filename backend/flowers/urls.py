from django.urls import path

from .views import bouquets, constructor, index, portfolio, showcase

app_name = 'flowers'

urlpatterns = [
    path('', index, name='index'),
    path('showcase', showcase, name='showcase'),
    path('bouquets', bouquets, name='bouquets'),
    path('constructor', constructor, name='constructor'),
    path('portfolio', portfolio, name='portfolio'),
]
