from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', views.home, name='home'),
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name = 'comment'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)