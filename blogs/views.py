from django.forms import forms
from .models import post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewCommentForm, SignUpForm
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
# Create your views here.


class BlogListView(ListView):
    model = post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = post
    template_name = 'post_detail.html'



class BlogCreateView(LoginRequiredMixin,CreateView):
    model= post 
    template_name = 'new_post.html'
    fields = ['title','body']
    login_url = 'login'

class CommentFormView(LoginRequiredMixin,CreateView):
    form_class = NewCommentForm
    model = post
    template_name = 'new_comment.html'
    login_url = 'login'
    success_url = 'home'

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.author= self.request.user
        self.object.posts= get_object_or_404(post)
        self.object.save()
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = post
    template_name= 'post_edit.html'
    fields = ['title', 'body']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model= post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    login_url = 'login'


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied        
        return super().dispatch(request, *args, **kwargs)
    


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url =reverse_lazy('login')
    template_name = 'registration/signup.html'