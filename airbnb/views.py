from django.shortcuts import render
from .models import airbnb
# Create your views here.
def all_posts(request):
    all_posts1=airbnb.objects.all()
    return render (request,'airbnbs/all_posts.html',{'post':all_posts1})
def single_post(request , post_id):
    single_post=airbnb.objects.get(id=post_id)
    return render (request,'airbnbs/single_posts.html',{'single':single_post})