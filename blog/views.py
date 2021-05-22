from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comments
from django.urls import reverse_lazy
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from .forms import CommentForm

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name= 'blog/home.html'
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('user')

class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'blog/add_comments.html'

    def form_valid(self, form):
        form.instance.post.id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('user')



class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()