from django.shortcuts import render, get_object_or_404

from .models import Article, Destination, Craft


def home(request):
    return render(request, 'culture/home.html')


def articles_list(request):
    articles = Article.objects.filter(
        status='published'
    )

    return render(request, 'culture/articles.html', {
        'articles': articles
    })


def article_detail(request, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        status='published'
    )

    return render(request, 'culture/article_detail.html', {
        'article': article
    })


def destinations_list(request):
    destinations = Destination.objects.all()

    return render(request, 'culture/destinations.html', {
        'destinations': destinations
    })


def destination_detail(request, slug):
    destination = get_object_or_404(
        Destination,
        slug=slug
    )

    return render(request, 'culture/destination_detail.html', {
        'destination': destination
    })


def crafts_list(request):
    crafts = Craft.objects.all()

    return render(request, 'culture/crafts.html', {
        'crafts': crafts
    })


def craft_detail(request, slug):
    craft = get_object_or_404(
        Craft,
        slug=slug
    )

    return render(request, 'culture/craft_detail.html', {
        'craft': craft
    })