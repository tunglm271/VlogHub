from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from django.contrib import messages
from .models import Profile,vlog,ProfileInfor, comment
from .forms import VlogForm, SignUpForm,PostProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def Index(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = request.user.id)
        form = VlogForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                new_vlog = form.save(commit=False)
                new_vlog.user = request.user
                new_vlog.save()
                messages.success(request,("You just post a new vlog!"))
                return redirect('/')
            a = request.POST['send']
            vlog_com = vlog.objects.get(id= a)
            com_content = request.POST['comment']
            new_com = comment(vlog=vlog_com,content=com_content,user= request.user)
            new_com.save()
            messages.success(request,("You just commemt a vlog!"))
        vlogs = vlog.objects.all().order_by('-created_at')
        return render(request,"polls/index.html",{'vlogs':vlogs,'form':form,'profile':profile})
    else:
        vlogs = vlog.objects.all().order_by('-created_at')
        return render(request,"polls/index.html",{'vlogs':vlogs})

def ProfileList(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = request.user.id)
        profiles = Profile.objects.exclude(user=request.user).order_by('-id')
        return render(request,'polls/Profile_list.html',{'profiles': profiles,'profile':profile})
    else:
        messages.success(request,("you need to sign in first!"))
        return redirect('/login/')
def Login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username= username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,("you Have Been Logged In! Start Vlogging!"))
            return redirect('/')
        else:
            messages.success(request,("Please try again!"))
            return render(request,'polls/pages-login.html')
    return render(request,'polls/pages-login.html')

def Logout(request):
    logout(request)
    messages.success(request,("See you again!"))
    return redirect('/login/')

def Register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("You succesfully register!"))
            return redirect('/')
    return render(request,'polls/pages-register.html',{'form':form})



def FQA(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = request.user.id)
        return render(request,'polls/pages-faq.html',{'profile':profile})
    else:
        return render(request,'polls/pages-faq.html')
def contact(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = request.user.id)
        return render(request,'polls/pages-contact.html',{'profile':profile})
    else:
        return render(request,'polls/pages-contact.html')
# Profile function
def ViewProfile(request,pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = pk)
        vlogs = vlog.objects.filter(user_id = pk).order_by('-created_at')
        if request.method == "POST":
            currtent_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                currtent_user_profile.follows.remove(profile)
            elif action == "follow":
                currtent_user_profile.follows.add(profile)
            currtent_user_profile.save()
        return render(request,'polls/profile.html',{'profile': profile,'vlogs': vlogs})
    else:
        messages.success(request,("you need to sign in first!"))
        return redirect('/login/')

def MyProfile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = request.user.id)
        Infor = ProfileInfor.objects.get(profile=profile)
        if request.method == "POST":
            q = PostProfile(request.POST, request.FILES,instance=Infor)
            if q.is_valid():
               q.save()
            return redirect('/My_profile/')
        form = PostProfile(instance=Infor)
        return render(request,"polls/users-profile.html",{'profile':profile,'form':form,})
    else:
        messages.success(request,("you need to sign in first!"))
        return redirect('/login/')

def unfollow(request,pk):
    profile = Profile.objects.get(user_id=pk)
    request.user.profile.follows.remove(profile)
    request.user.profile.save()
    return redirect(request.META.get("HTTP_REFERER"))

def follow(request,pk):
    profile = Profile.objects.get(user_id=pk)
    request.user.profile.follows.add(profile)
    request.user.profile.save()
    return redirect(request.META.get("HTTP_REFERER"))
# vlog interact funtion
def vlog_like(request, pk):
    if request.user.is_authenticated:
        Vlog = get_object_or_404(vlog,id=pk)
        if Vlog.likes.filter(id=request.user.id):
            Vlog.likes.remove(request.user)
        else:
            Vlog.likes.add(request.user)
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request,("you need to sign in first!"))
        return redirect('/login/')

def vlog_share(request,pk):
    if request.user.is_authenticated:
        Vlog = get_object_or_404(vlog,id=pk)
    return None

def delete_vlog(request,pk):
    Vlog = get_object_or_404(vlog,id=pk)
    if Vlog.user == request.user:
        Vlog.delete()
        messages.success(request,("The vlog has been deleted!"))
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request,("You don't own that vlog!"))
        return redirect('/')
def update_vlog(request,pk):
    Vlog = get_object_or_404(vlog,id=pk)
    if Vlog.user == request.user:
        form = VlogForm(request.POST or None,instance=Vlog)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,("Your Vlog has been updated!"))
                return redirect(request.META.get("HTTP_REFERER"))
        else:
            vlogs = vlog.objects.filter(user = request.user).order_by('-created_at').exclude(id = pk)
            profile = Profile.objects.get(user= request.user)
            return render(request,"polls/edit_vlog.html",{'vlogs':vlogs,'profile':profile,'form':form,'Vlog':Vlog})
    else:
        messages.success(request,("You don't own that vlog!"))
        return redirect('/')

def sreach(request):
    sreached = request.POST['query']
    UserScreach = User.objects.filter(username__contains = sreached)
    VlogSreach = vlog.objects.filter(content__contains = sreached)
    return render(request,"polls/sreached.html",{'sreached':sreached,'UserScreach':UserScreach,'VlogSreach':VlogSreach})