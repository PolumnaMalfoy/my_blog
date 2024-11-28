from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import *

# views.py
from django.shortcuts import render
from .models import Articles


def home(request):
    articles = Articles.objects.all()  # Fetch all articles from the database
    return render(request, 'home_page.html', {'articles': articles})


def articleView(request, id):
    if request.method == "GET":
        context = {
            'article': Articles.objects.get(id=id)

        }
        return render(request, 'article.html', context)


def admin(request):
    articles = Articles.objects.all()  # Fetch all articles from the database
    return render(request, 'admin.html', {'articles': articles})


def NewArticleView(request):
    if request.method == "GET":
        context = {

            "form": ArticleForm
        }
        return render(request, 'post-article.html', context)
    elif request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
        return redirect('new')


def EditArticleView(request, id):
    if request.method == "GET":
        context = {

            "article": Articles.objects.get(id=id)
        }
        return render(request, 'edit.html', context)
    elif request.method == "POST":
        pk = request.POST.get('pk')
        title = request.POST.get("title")
        #pub_date = request.POST.get("published_time")
        content = request.POST.get("content")

        article = Articles.objects.get(id=pk)
        #article.published_time = pub_date
        article.title = title
        article.content = content
        article.save()
        return redirect('admin')
