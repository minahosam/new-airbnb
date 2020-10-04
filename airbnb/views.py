from django.shortcuts import redirect, render
from .models import airbnb
from .forms import FormPost
from django import http
# Create your views here.
def all_posts(request):
    all_posts1=airbnb.objects.all()
    return render (request,'airbnbs/all_posts.html',{'post':all_posts1})
def single_post(request , post_id):
    single_post=airbnb.objects.get(id=post_id)
    return render (request,'airbnbs/single_posts.html',{'single':single_post})
def new_post(request):
    if request.method == "POST":##save
        print('save')
        form=FormPost(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=FormPost
        print('new page')
    return render (request,'airbnbs/new_post.html',{'form':form})
def post_edit(request , post_id ):
    single_post=airbnb.objects.get(id=post_id)
    if request.method == "POST":##save
        print('edit')
        form=FormPost(request.POST , request.FILES , instance=single_post)## instance=single_post to save the edit in the intial post
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect('')## this command save edited post as new posts

    else:
        form=FormPost(instance=single_post)
        print('new page')
    return render (request,'airbnbs/edit_post.html',{'form':form})
def post_delete(request , post_id ):
    single_post=airbnb.objects.get(id=post_id)
    single_post.delete()
    return redirect('/rooms')
