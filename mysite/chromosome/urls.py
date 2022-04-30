from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/chromosome
    path('', views.abnormal_list, name='abnormal_list'),
    path('<int:abnormal_pk>', views.abnormal_detail, name='abnormal_detail'),
    path('abnormal_upload', views.abnormal_upload, name='abnormal_upload'),
    path('type/<int:abnormal_type_pk>', views.abnormal_with_type, name='abnormal_with_type'),
    path('date/<int:year>/<int:month>', views.abnormal_with_date, name="abnormal_with_date"),
    path('upload_pdf/<int:abnormal_pk>', views.upload_pdf, name='upload_pdf'),
    path('reference/<int:abnormal_pk>', views.abnormal_reference, name='abnormal_reference'),
]