from django.urls import path
from django.urls.conf import include
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView, PostViewSet
from django.conf.urls.static import static
from django.conf import settings


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, "post")

urlpatterns = [
    path('',HomeView.as_view(), name='user'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('article/<int:pk>edit', UpdatePostView.as_view(), name = 'update'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name = 'comment'),
    path('signup/', views.signup, name='signup'),
    # path('api/v1/posts/', PostViewSet.as_view() ),
    # path('api/v1/posts/<int:pk>', views.post_element)
    path('api/', include(router.urls)),
]