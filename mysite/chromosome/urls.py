from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/chromosome
    path('', views.abnormal_list, name='abnormal_list'),
    path('<int:abnormal_pk>', views.abnormal_detail, name='abnormal_detail'),
    # path('type/<int:blog_type_pk>', views.blogs_with_type, name='blogs_with_type'),
    # path('date/<int:year>/<int:month>', views.blogs_with_date, name="blogs_with_date"),
]