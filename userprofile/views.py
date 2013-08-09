from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
       auth.login(request, user)
       return HttpResponseRedirect('/user/loggedin/')
    else:
       return HttpResponseRedirect('/user/invalid/')
        
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('registration/login.html', c)
    
def loggedin(request):
    return render_to_response('registration/loggedin.html', 
                             {'full_name': request.user.username})
                             
def invalid(request):
    return render_to_response('registration/invalid.html')
    
def logout(request):
    auth.logout(request)
    return render_to_response('registration/logout.html')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/user/register_success/')
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = UserCreationForm()
    
    return render(request, 'registration/register.html', args)
    
def register_success(request):
    return render_to_response('registration/register_success.html')
