from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:post_id>/post/',views.getPost,name='post'),
    path('category/',views.getCategories,name='categories'),
    path('category/<int:category_id>/category', views.getCategory,name="category"),
    path('post_list/',views.PostListView.as_view(),name='post_list'),
    #path('post_list/', views.PostListView.as_view(),name="post_list"),
    path('post_details/<int:pk>/',views.PostDetailView.as_view(),name="post_details"),
    #path('post_details/<int:id>/',views.PostDetailView.as_view(),name="post_details")
    path('simple_view/',views.SimpleView.as_view(),name="simple_view" )
]
