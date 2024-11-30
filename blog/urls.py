from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [                             
    path('', PostListView.as_view(), name='home'), #Esto es el post-list
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #Esto es el post-detail
]