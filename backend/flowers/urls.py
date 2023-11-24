from django.conf.urls.static import static
from django.urls import path

from .views import bouquets, constructor, delivery, index, portfolio, showcase
from flowerstore.settings import MEDIA_ROOT, MEDIA_URL

app_name = 'flowers'

urlpatterns = [
    path('', index, name='index'),
    path('showcase', showcase, name='showcase'),
    path('bouquets', bouquets, name='bouquets'),
    path('constructor', constructor, name='constructor'),
    path('portfolio', portfolio, name='portfolio'),
    path('delivery', delivery, name='delivery'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
