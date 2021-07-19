from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post
from django.http import HttpResponseRedirect

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'



def post_admin(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/admin')


from .models import Post

from django.shortcuts import render, get_object_or_404

