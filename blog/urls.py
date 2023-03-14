from django.urls import path
from .import views
from blog.views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create-post/', PostCreateView.as_view(), name='post-create'),
    path('update-post/<int:pk>', PostUpdateView.as_view(), name='post-update'),
    path('delete-post/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about ,name='blog-about'),
]


