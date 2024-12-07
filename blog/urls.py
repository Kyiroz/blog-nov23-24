from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from .views import PostUpdateView, PostDeleteView
urlpatterns = [                             
    path('', PostListView.as_view(), name='home'), #Esto es el post-list
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #Esto es el post-detail, el int:pk es el ID
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]