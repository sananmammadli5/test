from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexview.as_view(),name='indexpage'),
    path('create',views.create_post.as_view(),name='createpage'),
    path('<int:pk>',views.detail.as_view(),name='detailpage'),
    path('<int:pk>/edit',views.editview.as_view(),name='editpage'),
    path('<int:pk>/delete',views.delete.as_view(),name='deletepage'),
]