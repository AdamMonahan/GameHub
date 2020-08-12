from django.shortcuts import render, redirect
from login.models import User

# Create your views here.
def discuss(request):
    if 'user_id' not in request.session:
        return redirect('/') 
    context = {
        'user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'discussions/index.html', context)