from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *


def allArticles(request):
    titlesOfArticles = Article.objects.all()
    return render(request, 'articles/articles.html', {'titlesOfArticles': titlesOfArticles,'title': 'Статьи'})


def healthArticles(request):
    titlesOfArticles = Article.objects.filter(category=1)
    return render(request, 'articles/articles_health.html', {'titlesOfArticles': titlesOfArticles, 'title': 'Статьи про здоровье'})


def devicesArticles(request):
    titlesOfArticles = Article.objects.filter(category=3)
    return render(request, 'articles/articles_devices.html', {'titlesOfArticles': titlesOfArticles, 'title': 'Статьи про девайсы'})


def foodArticles(request):
    titlesOfArticles = Article.objects.filter(category=4)
    return render(request, 'articles/articles_food.html', {'titlesOfArticles': titlesOfArticles, 'title': 'Статьи про питание'})


def sportArticles(request):
    titlesOfArticles = Article.objects.filter(category=2)
    return render(request, 'articles/articles_sport.html', {'titlesOfArticles': titlesOfArticles, 'title': 'Статьи про спорт'})


def showCertainArticle(request, art_slug):
    article = get_object_or_404(Article, slag=art_slug)
    return render(request, 'articles/certain_article.html', {'article': article})
