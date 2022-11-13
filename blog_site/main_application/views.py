import datetime
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .serializers import *

# Create your views here.
def index(request):
    displayed_articles = Article.objects.all().order_by('date').reverse()[:10]
    comments = {}
    for art in list(displayed_articles):
        comments[art.pk] = list(Comment.objects.filter(article=art.pk))

    print(comments)

    comments_form = CommentForm()
    return render(request, 'main_application/index.html', {'displayed_articles': displayed_articles,
                                                            'comments_form' : comments_form,
                                                            'comments' : comments})

def logout_user(request):
    logout(request)
    return redirect(index)

#Displays a Login form to log the user in.  If the user is already logged in, then the index page is shown and they are greeted.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticates user based on data entered from the form.
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(index)
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        form = LoginForm()
        return render(request, 'main_application/login.html', 
            {'form' : form})


def new_post(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        date = datetime.datetime.now()
        new_article = Article(article_title=title, body=body, date=date)
        new_article.save()
        return HttpResponseRedirect('/')
    else:
        form = ArticleForm()
        return render(request, 'main_application/new_post.html', {'form':form})

def edit_post(request, id):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        date = datetime.datetime.now()
        modified_article = Article.objects.get(pk=id)
        modified_article.body = body
        modified_article.date = date
        modified_article.article_title = title
        modified_article.save()
        return HttpResponseRedirect('/')
    else:
        article = Article.objects.get(pk=id)
        form = ArticleForm(initial={'title': article.article_title, 'body' : article.body})
        return render(request, 'main_application/edit_post.html', {'article' : article, 'form' : form})

def post_comment(request, id):
    if request.method == "POST":
        date = datetime.datetime.now()
        article = Article.objects.get(pk=id)
        body = request.POST['body']
        new_comment = Comment(date=date, article=article, body=body)
        new_comment.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def api_get_recent_articles(request, page_num):
    displayed_articles = Article.objects.all().order_by('date').reverse()[(page_num-1) * 5 :page_num * 5]
    print(page_num)
    data = {}
    for article in displayed_articles:
        data[article.pk] = ArticleSerializer(article).data

        comments_query_set = Comment.objects.filter(article=article.pk)
        comments = []
        
        for comment in comments_query_set:
            comment = CommentSerializer(comment).data
            comments.append(comment)
        data[article.pk]['comments'] = comments

    return JsonResponse(data)