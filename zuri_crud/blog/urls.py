from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostview, UpdatePostView, DeletePostView, AddCommentView

urlpatterns = [
    #path('', views.home, name='home'),
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name = 'comment'),
    path('signup/', views.signup, name='signup'),


]