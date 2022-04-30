import random, datetime

from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum, Q
from django.core.paginator import Paginator
from django.core.cache import cache
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from django.contrib import auth
from django.contrib.auth.models import User

from blog.models import Motto, Blog
from chromosome.models import Abnormal


def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
                .filter(read_details__date__lt=today, read_details__date__gte=date) \
                .values('id', 'title') \
                .annotate(read_num_sum=Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:7]

def get_7_days_hot_abnormals():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    abnormals = Abnormal.objects \
                .filter(read_details__date__lt=today, read_details__date__gte=date) \
                .values('id', 'karyotype') \
                .annotate(read_num_sum=Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return abnormals[:7]

def home(request):
    n = 1
    i = random.randint(0, Motto.objects.count() - n)
    abnormal_content_type = ContentType.objects.get_for_model(Abnormal)
    dates, read_nums = get_seven_days_read_data(abnormal_content_type)
    # 获取7天热门博客的缓存数据
    hot_abnormals_for_7_days = cache.get('hot_abnormals_for_7_days')
    if hot_abnormals_for_7_days is None:
        hot_abnormals_for_7_days = get_7_days_hot_abnormals()
        cache.set('hot_abnormals_for_7_days', hot_abnormals_for_7_days, 3600)

    context = {'motto': Motto.objects.all()[i], 'dates': dates, 'read_nums': read_nums,
               'today_hot_data': get_today_hot_data(abnormal_content_type),
               'yesterday_hot_data': get_yesterday_hot_data(abnormal_content_type),
               'hot_abnormals_for_7_days': hot_abnormals_for_7_days}

    return render(request, 'home.html', context)


def search(request):
    search_words = request.GET.get('wd', '').strip()
    # 分词：按空格 & | ~
    condition = None
    for word in search_words.split(' '):
        if condition is None:
            condition = Q(karyotype__icontains=word)
        else:
            condition = condition | Q(karyotype__icontains=word)

    search_blogs = []
    if condition is not None:
        # 筛选：搜索
        search_blogs = Abnormal.objects.filter(condition)

    # 分页
    paginator = Paginator(search_blogs, 20)
    page_num = request.GET.get('page', 1)  # 获取url的页面参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['search_words'] = search_words
    context['search_blogs_count'] = search_blogs.count()
    context['page_of_blogs'] = page_of_blogs
    return render(request, 'search.html', context)

