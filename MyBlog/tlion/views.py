import markdown2
from . import models
from . models import Article, Category, Tag
from django.shortcuts import render, get_object_or_404, redirect
from comments.forms import CommentForm
from comments.models import Comment
from .forms import ArticleForm
from django.http import HttpResponse
import os
import datetime


def index(request):

    articles = Article.objects.filter(status='p')
    for article in articles:
        article.content = markdown2.markdown(article.content)
    context = {
        'articles': articles
    }
    return render(request, 'tlion/index.html', context=context)


def article_page(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.content = markdown2.markdown(article.content)
    form = CommentForm()
    comments = Comment.objects.filter(article=article)

    context = {
        'article': article,
        'form': form,
        'comments': comments
    }

    return render(request, 'tlion/article_page.html', context=context)


def edit_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'tlion/edit_page.html', {'article': article})


def edit_action(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form_data = form.cleaned_data
            # 自定义图片上传

            # 但是在views也保存了一份,我们给他改掉改成我们自己的就行了
            article = form.save(commit=False)

            article.head_img = form_data['head_img']
            excer = article.content[:200] + '...'
            article.excerpt = excer

            article.save()
            form = CommentForm()

            context = {
                'form': form,
                'article': article
            }

            return render(request, 'tlion/article_page.html', context=context)

        else:
            context = {
                       'form': form,
                       }
            return render(request, 'tlion/edit_new_page.html', context=context)
    form = ArticleForm()
    context = {
        'form': form,
    }

    return render(request, 'tlion/edit_new_page.html', context=context)


'''def handle_upload_file(f, request):

    # f这里获取到文件句柄

    base_img_upload_path = 'static/tlion/uploads'
    user_path = "%s/%s" % (base_img_upload_path, request.author.name)

    if not os.path.exists(user_path):
        os.mkdir(user_path)

    with open('%s/%s' % (user_path, f.name), 'wb+') as destinations:
        for chunk in f.chunks():
            destinations.write(chunk)

    return "/static/Uploads/%s/%s" % (request.user.userprofile.id, f.name)'''


def modify_action(request):
    article_id = request.POST.get('article_id')
    article = models.Article.objects.get(pk=article_id)
    article.title = request.POST.get('title')
    content = request.POST.get('content')

    article.status = request.POST.get('select')
    article.content = content
    article.excerpt = content[:200]
    article.save()

    article.content = markdown2.markdown(article.content)

    form = CommentForm()
    comments = Comment.objects.filter(article=article)

    context = {'article': article,
               'form': form,
               'comments': comments,
    }
    return render(request, 'tlion/article_page.html', context=context)


def archives(request, year, month):
    articles = Article.objects.filter(create_time__year=year, create_time__month=month)
    return render(request, 'tlion/index.html', {'articles': articles})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    articles = Article.objects.filter(category=cate)
    return render(request, 'tlion/index.html', {'articles': articles})


def tag(request, pk):
    tag_ = get_object_or_404(Tag, pk=pk)
    articles = Article.objects.filter(tag=tag_)
    return render(request, 'tlion/index.html', {'articles': articles})


def contact(request):
    return render(request, 'tlion/contact.html')


def thumb_up(request):
    return request(request, '')


def collect_likes(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    liked_article = request.session.get(article_id)

    if article_id != liked_article:
        article.likes += 1
        article.save()
        request.session[article_id] = article_id
        return redirect(article)

    return redirect(article)


def collect_views(request):

    pk = request.get['pk']
    article = Article.objects.filter(pk=2)

    last_view = request.session.get('last_view')  # 获取最后一次浏览本站的时间last_view
    if last_view:
        last_visit_time = datetime.datetime.strptime(last_view[:-7], "%Y-%m-%d %H:%M:%S")
        if datetime.datetime.now() >= last_visit_time + datetime.timedelta(minutes=5):  # 判断如果最后一次访问网站的时间大于5分钟，则浏览量+1
            article.views += 1
            article.save()
    else:
        article.views += 1
        article.save()
    request.session['last_view'] = str(datetime.datetime.now())



