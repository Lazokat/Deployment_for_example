from django.urls import path
from .views import BlogView,BlogCreate,BlogDelete,BlogDetail,BlogUpdate,BlogDetail
urlpatterns=[
    path('',BlogView.as_view(),name='all_list'),
    path('<int:pk>/update/',BlogUpdate.as_view(),name='blog_update'),
    path('<int:pk>/delete/',BlogDelete.as_view(),name='blog_delete'),
    path('<int:pk>/detail/',BlogDetail.as_view(),name='blog_detail'),
    path('create/',BlogCreate.as_view(),name='blog_create'),
]