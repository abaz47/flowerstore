from django.shortcuts import render

from .labels import LABELS
from .models import Flower
from .settings import MEDIA_URL


def index(request):
    return render(
        request,
        'index.html',
        {
            'labels': LABELS,
        }
    )


def showcase(request):
    return render(
        request,
        'showcase.html',
        {
            'flowers': Flower.objects.filter(is_visible=True),
            'labels': LABELS,
            'media_url': MEDIA_URL,
        }
    )


def bouquets(request):
    return render(
        request,
        'bouquets.html',
        {
            'labels': LABELS,
        }
    )


def constructor(request):
    return render(
        request,
        'constructor.html',
        {
            'labels': LABELS,
        }
    )


def portfolio(request):
    return render(
        request,
        'portfolio.html',
        {
            'labels': LABELS,
        }
    )


def delivery(request):
    return render(
        request,
        'delivery.html',
        {
            'labels': LABELS,
        }
    )
