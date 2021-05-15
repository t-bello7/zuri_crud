from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import serializers
from .models import Post, Comments
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm, CommentForm

# Create your views here.
#def home(request):
#    return render(request,'home.html',{})
#homeView for list
class HomeView(ListView):
    model = Post
    template_name= 'user.html'
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('user')

class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'add_comments.html'

    def form_valid(self, form):
        form.instance.post.id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('user')


def signup(request):
    form_class = UserCreateForm
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('user')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})

# @api_view(['GET'])
# def post_collection(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many =True)
#         content ={
#             "posts": serializer.data,
#         }
#         return Response(content)

# @api_view(['GET'])
# def post_element(request, pk):
#     try: 
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()