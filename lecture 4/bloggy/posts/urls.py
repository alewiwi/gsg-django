from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:post_id>/post/',views.getPost,name='post'),
    path('category/',views.getCategories,name='categories'),
    path('category/<int:category_id>/category', views.getCategory,name="category")
]
