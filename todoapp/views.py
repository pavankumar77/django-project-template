from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponseRedirect
from todoapp.signin_form import UserForm
from django.views.decorators.csrf import csrf_exempt

from todoapp.models import Tasks
from django.contrib.auth import authenticate,login





def tasks(request):
 
    data = Tasks.objects.all()
    return render_to_response('index.html',{'task':data})

def filter_by_status(request):
    data = Tasks.objects.filter(task_accessibility='public',task_status='open') 
    return render_to_response('index.html',{'task':data})


def fiter_by_accessibility(request):
    
    data =Tasks.objects.filter(task_accessibility='public')
    return render_to_response('index.html',{'task':data})

   
def user(request):
    
    data =Tasks.objects.filter(user_name = request.user.id , task_accessibility='public' )
#    data1 =Tasks.objects.filter(task_accessibility='public')
    return render_to_response('index.html',{'task':data})



def create_task(request):
    
    return HttpResponse('Coming Soon')

def registration(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        user_form = UserForm()
    return render_to_response('registration.html',
            {'user_form': user_form, 'registered': registered}, context)




@csrf_exempt
def sign_in(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
            login(request,user)
           # data = Tasks.objects.filter(task_accessibility='public',task_status='open')
            return HttpResponseRedirect('/user')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('signin.html', {}, context)
    














'''
def signin(request):
    c={}
    c.update(csrf(request))
    return render_to_response('signin.html',c)


def auth_view(request):
    username = request.POST.get('username','')
    password =request.POST.get('password','')
    user =auth .authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/admin/loggeddin')
    else:
        return HttpResponseRedirect('/admin/invalid')

def  loggedin (request):
    return render_to_response('signedin.html')
 
def logout(request):
    auth.logout(request)
    return HttpResponse('logged out')
 '''