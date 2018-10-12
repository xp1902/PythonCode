from django.shortcuts import render, get_object_or_404, redirect
from tlion.models import Article

from .models import Comment
from .forms import CommentForm


def article_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        # 我们利用这些数据构造了 CommentForm 的实例，这样 django 的表单就生成了
        form = CommentForm(request.POST)

        # 当调用 form.is_valid() 方法时，django 自动帮我们检查表单的数据是否符合格式要求
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例
            # 但还不保存数据到数据库
            article.comments_num = article.comments_num + 1
            article.save()
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.article = article
            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()

            # 重定向到 post 的详情页
            return redirect(article)

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误
            # 因此我们传了三个模板变量给 detail.html
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论
            # 因为 Post 和 Comment 是 ForeignKey 关联的
            # 因此使用 post.comment_set.all() 反向查询全部评论
            # 正向查询就直接是 comment.post
            comments = Comment.objects.filter(article=article)
            context = {'article': article,
                       'form': form,
                       'comments': comments
                       }
            return render(request, 'tlion/article_page.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(article)


def comment_reply(request):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        # 我们利用这些数据构造了 CommentForm 的实例，这样 django 的表单就生成了
        form = CommentForm(request.POST)

        # 当调用 form.is_valid() 方法时，django 自动帮我们检查表单的数据是否符合格式要求
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例
            # 但还不保存数据到数据库
            article.comments_num = article.comments_num + 1
            article.save()
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.article = article
            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()

            # 重定向到 post 的详情页
            return redirect(article)

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误
            # 因此我们传了三个模板变量给 detail.html
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论
            # 因为 Post 和 Comment 是 ForeignKey 关联的
            # 因此使用 post.comment_set.all() 反向查询全部评论
            # 正向查询就直接是 comment.post
            comments = Comment.objects.filter(article=article)
            context = {'article': article,
                       'form': form,
                       'comments': comments
                       }
            return render(request, 'tlion/article_page.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(article)
