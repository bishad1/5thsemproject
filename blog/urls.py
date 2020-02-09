from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/Update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/Delete', PostDeleteView.as_view(), name='post-delete')
]
