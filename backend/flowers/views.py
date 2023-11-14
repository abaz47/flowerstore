from django.shortcuts import render


def index(request):
    return render(
        request,
        'index.html'
    )


def showcase(request):
    return render(
        request,
        'showcase.html'
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
