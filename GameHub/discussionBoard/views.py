from django.shortcuts import render, redirect
from login.models import User
from discussionBoard.models import Posts
from django.contrib import messages

# Create your views here.
def discuss(request):
    if 'user_id' not in request.session:
        return redirect('/') 
    context = {
        'user': User.objects.get(id = request.session['user_id']),
        'posts': Posts.objects.all(),
    }
    return render(request, 'discussions/index.html', context)

def delete(request, post_id):
    to_delete = Posts.objects.get(id=post_id)
    if to_delete.author_id == request.session['user_id']:
        to_delete.delete()
    return redirect('/discuss')

def create(request):
    errors = Posts.objects.validate(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/discuss')
    new_post = Posts.objects.create(title=request.POST['title'], content=request.POST['content'], author=User.objects.get(id=request.session['user_id']))
    #new_post.author = request.session['user_id']
    #request.session['user_id'] = new_post.id
    return redirect('/discuss')