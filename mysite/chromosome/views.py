
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.conf import settings
from .models import Abnormal, AbnormalType
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import read_statistics_once_read
from django.urls import reverse

from comment.models import Comment
from comment.forms import CommentForm
from .forms import AbnormalForm


# Create your views here.
def get_abnormals_list_common_data(request, abnormals_all_list):
    paginator = Paginator(abnormals_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1)  # 获取url的页码参数（GET请求）
    page_of_abnormals = paginator.get_page(page_num)
    current_page_num = page_of_abnormals.number  # 获取当前页码

    # 获取当前页面前后各2页的页码范围
    page_range = [x for x in range(current_page_num - 2, current_page_num + 3) if x in paginator.page_range]
    # 获取日期归档对应的博客数量
    abnormal_dates = Abnormal.objects.dates('created_time', 'month', order="DESC")
    abnormal_date_dict = {}
    for abnormal_date in abnormal_dates:
        abnormal_count = Abnormal.objects.filter(created_time__year=abnormal_date.year,
                                         created_time__month=abnormal_date.month).count()
        abnormal_date_dict[abnormal_date] = abnormal_count
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {'abnormals': page_of_abnormals.object_list, 'page_of_abnormals': page_of_abnormals, 'page_range': page_range,
               'abnormal_types': AbnormalType.objects.annotate(abnormal_count=Count('abnormal')),
               'abnormal_dates': abnormal_date_dict}
    return context

def abnormal_list(request):
    abnormals_all_list = Abnormal.objects.all()
    context = get_abnormals_list_common_data(request, abnormals_all_list)
    return render(request, 'chromosome/abnormal_list.html', context)

def abnormal_detail(request, abnormal_pk):
    context = {}
    abnormal = get_object_or_404(Abnormal, pk=abnormal_pk)
    read_cookie_key = read_statistics_once_read(request, abnormal)
    abnormal_content_type = ContentType.objects.get_for_model(abnormal)
    comments = Comment.objects.filter(content_type=abnormal_content_type, object_id=abnormal.pk)

    context['previous_abnormal'] = Abnormal.objects.filter(created_time__gt=abnormal.created_time).last()
    context['next_abnormal'] = Abnormal.objects.filter(created_time__lt=abnormal.created_time).first()
    context['abnormal'] = abnormal
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={'content_type': abnormal_content_type.model, 'object_id': abnormal_pk})
    response = render(request, 'chromosome/abnormal_detail.html', context)
    response.set_cookie(read_cookie_key, 'true')
    return response

def abnormal_upload(request):
    if request.method == 'POST':
        abnormal_form = AbnormalForm(request.POST, request.FILES)
        if abnormal_form.is_valid():
            obj = abnormal_form.save(commit=False)
            obj.author = request.user
            obj.save()
            abnormal_form.save_m2m()

            return redirect('abnormal_list')
    else:
        abnormal_form = AbnormalForm()

    context = {}
    context['abnormal_form'] = abnormal_form
    return render(request, 'chromosome/abnormal_upload.html', context)
