from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all().order_by('published_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})
    
