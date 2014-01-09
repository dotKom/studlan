#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import translation
from django.http import HttpResponseRedirect

from studlan.news.models import Article


def main(request, page):
    objects = Article.objects.all()

    articles = []

    for article in objects:
        articles.append(article.get_translation(language=translation.get_language()))
    paginator = Paginator(articles, 10) #Articles per page

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:

        # If page is not an integer, deliver first page.

        articles = paginator.page(1)
    except EmptyPage:

        # If page is out of range (e.g. 9999), deliver last page of results.

        articles = paginator.page(paginator.num_pages)
    except:

        # If no page is given, show the first

        articles = paginator.page(1)


    return render(request, 'news/news.html', {'articles': articles, 'page': page})


def single(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article = article.get_translation(language=translation.get_language())
    return render(request, 'news/single.html', {'article': article})

