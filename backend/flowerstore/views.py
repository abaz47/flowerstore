from django.shortcuts import render

from .settings import MEDIA_URL
from .models import Flower


def index(request):
    return render(
        request,
        'index.html'
    )


def showcase(request):
    return render(
        request,
        'showcase.html',
        {
            'media_url': MEDIA_URL,
            'flowers': Flower.objects.filter(is_visible=True)
        }
    )


def bouquets(request):
    return render(
        request,
        'bouquets.html'
    )


def constructor(request):
    return render(
        request,
        'constructor.html'
    )


def portfolio(request):
    return render(
        request,
        'portfolio.html'
    )


def delivery(request):
    return render(
        request,
        'delivery.html'
    )
