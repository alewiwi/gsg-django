from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:post_id>/post/',views.getPost,name='post'),
    path('<int:category_id>/category/',views.getPost,name='category'),
]
