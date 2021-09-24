from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth

# Create your views here.
def index(request):
    #return  HttpResponse("Hello Django!")
    return   render(request,"index.html")

def login_action(request):
    print("测试开始啦")
    if request.method=='POST':
       username =request.POST.get('username','')
       password =request.POST.get('password','')
       user=auth.authenticate(username=username,password=password)
       if user  is not None:
           auth.login(request,user)
       #if username=='admin' and password=='admin123':
           #return  HttpResponseRedirect('/event_manage/')
           #response.set_cookie("user",username,3600)   #添加浏览器cookie
           response=HttpResponseRedirect('/event_manage/')
           request.session['user']=username  #讲session记录到浏览器
           return response
       else:
           return render(request,'index.html',{'error':'username or password error!'})
@login_required
def event_manage(request):
     #username=request.COOKIES.get('user','')  #读取cookies
     username=request.session.get('user','')   #读取session
     return render(request,"event_manage.html",{"user":username})