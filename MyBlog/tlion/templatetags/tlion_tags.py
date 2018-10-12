from django import template
import time
import datetime
from ..models import Article, Category, Tag
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all()[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    categories = Category.objects.all()
    return categories


@register.simple_tag
def get_comments_num(pk):
    article = Article.objects.get(pk=pk)
    return len(article.comment_set)


@register.simple_tag
def get_time():
    return time.ctime()


@register.simple_tag
def get_count():
    countfile = open('count.dat', 'a+')  # 以读写形式打开记录计数的文件
    counttext = countfile.read()
    try:
        count = int(counttext) + 1

    except:
        count = 1
    countfile.seek(0)
    countfile.truncate()  # 清空文件
    countfile.write(str(count))  # 重新写入新的访问量
    countfile.flush()
    countfile.close()
    return count


@register.simple_tag
def get_tags():
    tags = Tag.objects.all()
    return tags


def tree_search(d_dic, comment):
    # 这里不用传附近和儿子了因为他是一个对象,可以直接找到父亲和儿子
    for k, v_dic in d_dic.items():
        if k == comment.parent_comment:
            # 如果找到了
            d_dic[k][comment] = {}
            # 如果找到父亲了,你的把自己存放在父亲下面,并把自己当做key,value为一个空字典
            return
        else:
            # 如果找不到递归查找
            tree_search(d_dic[k], comment)


def generate_comment_html(sub_comment_dic, margin_left_val):
    # 先创建一个html默认为空
    html = ""
    for k, v_dic in sub_comment_dic.items():
        # 循环穿过来的字典
        # 下面的只是把第一层加了他可能还有儿子,所以通过递归继续加
        t = str(k.pub_time.strftime("%Y-%m-%d %H:%I:%S"))
        html += "<li class='comment-item' style='margin-left:%spx'><span class='name'>" % margin_left_val + k.name \
                + "</span><time class='date'>" \
                + str(t) + "</time>" \
                + "<div class='text'>" \
                + k.content \
                + "</div>" \
                + "<div class='comment-notes'>" \
                + "<p align='right' id='reply'>回复</p>" \
                 \
                + "</li>"
        if v_dic:
            html += generate_comment_html(v_dic, margin_left_val+15)
    return html


@register.simple_tag
def build_comment_tree(comments):

    comment_dic = {}

    for comment in comments:
        # 每一个元素都是一个对象
        if comment.parent_comment is None:
            # 如果没有父亲
            comment_dic[comment] = {}
        else:
            # 通过递归找
            tree_search(comment_dic, comment)

    # #测试:
    # for k,v in comment_dic.items():
    #     print(k,v)

    # 上面完成之后开始递归拼接字符串

    # div框架
    html = "<div class='comment-box'>"
    margin_left = 0
    for k, v in comment_dic.items():
        # 第一层的html
        t = str(k.pub_time.strftime("%Y-%m-%d %H:%I:%S"))
        html += "<li class='comment-item'><span class='name'>" + k.name + "</span><span class='date'>" + t + "</span>" \
                + "<div class='text'>" \
                + k.content \
                + "</div>" \
                + "<div class='comment-notes'>" \
                + "<p align='right' id='reply' style='color:green;font-size:16px;'>回复</p>" \
                + "</li>"
        '''+ "<div class='Main'>" \
                + "<div class='Input_Box' id='reply-box'> "\
                + "<textarea class='Input_text'></textarea>"\
                + "<div class='faceDiv'> </div>"\
                + "<div class='Input_Foot'> <a class='imgBtn' href='javascript:void(0);'></a><a class='postBtn'>确定</a> </div>"\
                + "</div>" \
                + "</div>" \ '''
        # 通过递归把他儿子加上
        html += generate_comment_html(v, margin_left+15)
    return mark_safe(html)


'''@register.simple_tag
def collect_views(request):
    pk = request.GET['pk']
    article = Article.objects.filter(pk=pk)
    last_view = request.session.get('last_view')  # 获取最后一次浏览本站的时间last_view
    if last_view:
        last_visit_time = datetime.datetime.strptime(last_view[:-7], "%Y-%m-%d %H:%M:%S")
        if datetime.datetime.now() >= last_visit_time + datetime.timedelta(minutes=5):  # 判断如果最后一次访问网站的时间大于5分钟，则浏览量+1
            article.views += 1
            article.save()
    else:
        article.views += 1
        article.save()
    request.session['last_view'] = str(datetime.datetime.now())'''
