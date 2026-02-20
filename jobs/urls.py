from django.urls import path
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    ApplyJobView,
)

urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('create/', JobCreateView.as_view(), name='job-create'),
    path('apply/', ApplyJobView.as_view(), name='apply-job'),
]
