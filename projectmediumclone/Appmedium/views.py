from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import *
from django.db.models import Q
def index(request):

    return render(request,'index.html')

def Home(request):
    posts = PostCreate.objects.all()
    posts_ordey = PostCreate.objects.all().order_by("?")[:3]
    profil = Profil.objects.get(user=request.user)
    context={
        'posts':posts,
        'posts_ordey':posts_ordey,
        'profil':profil,
    }
    return render(request,'home.html',context)

def Login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.warning(request,'Username or Password is incorrect')



    return render(request,'login.html')

def Register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        Repassword = request.POST.get("password_confirm")
        

        if password == Repassword:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username,first_name = first_name,last_name=last_name,email=email,password=password)
                    user.save()
                    profil = Profil.objects.create(user=user)
                    profil.save()
                    return redirect("login")
                else:
                    messages.warning(request,'The e-mail address you entered is being used by someone else.')
            else:
                messages.warning(request,'The username you entered is being used by someone else.')
        else:
            messages.warning(request,'Passwords Incompatible')

    return render(request,'register.html')

def Logout(request):
    logout(request)
    return redirect("index")


def Post_Create(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST.get("title")
            image = request.FILES.get("image")
            description = request.POST.get("description")

            post = PostCreate.objects.create(user=request.user,title=title,image=image,description=description)
            post.save()
            return redirect("home")
    else:
        return redirect("login")

    

    return render(request, 'post_create.html')

def Post(request,id):
    post = PostCreate.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    print(comments)
    if request.method == "POST":
        text = request.POST.get('comment')

        comment = Comment.objects.create(user=request.user,text=text,post=post)
        comment.save()
        return redirect('/post_detay/' + id)
    context={
        'post':post,
        'comments':comments,
    }

    

    return render(request, 'post_detay.html',context)

def Profile(request,id):
    user = User.objects.get(id=id)
    profil = Profil.objects.get(user=user)
    posts = PostCreate.objects.filter(user=user)

    if request.method == "POST":
        about = request.POST.get("about")
        image = request.FILES.get("image")
        if not image:
            image = profil.image
        profil.about=about
        profil.image=image
        profil.save()
        return redirect("/profile/" + id)
    context={
        'user':user,
        'posts':posts,
        'profil':profil,
    }
    return render(request, 'profile.html',context)

def search(request):
    if "q" in request.GET and request.GET['q'] != "":
        q = request.GET['q']
        posts = PostCreate.objects.filter(Q(title__contains=q) | Q(description__icontains=q))
        print(posts)
    else:
        return redirect('home')
    
    return render(request, 'home.html',{
        'posts':posts
    })