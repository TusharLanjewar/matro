from django.shortcuts import render,redirect
from website.models import *
from website.forms import *
from django.contrib.auth import login,authenticate
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def loginpage(request):
        return render(request,"loginpage.html")
def about(request):
        return render(request,"about.html")
def search(request):
    return render(request,"search.html")
def membership(request):
    return render(request,"membership.html")
def contact(request):
    return render(request,"contact.html")
def happystories(request):
    return render(request,"happystories.html")
def faq(request):
    return render(request,"faq.html")
def terms(request):
    return render(request,"terms.html")
def privacy(request):
    return render(request,"privacy.html")
def disclaimer(request):
    return render(request,"disclaimer.html")
def register(request):
    
    return render(request,"register.html")
def blogss(request):
    return render(request,"blogs.html")

def searchdetail(request):
   return render(request,"searchdetail.html")

    
def apply(request):
    if request.method=="POST":
        form=contacts(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/')
    return render(request,'contact.html')
    
def insertregister(request):
    if request.method=="POST":
        form=searchsform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/membership/')
    return render(request,'register.html')
    
def blogss(request):
    bl=blogs.objects.all()
    context={'bl':bl}
    return render(request,'blogs.html',context)
    
def blogdetail(request,id):
    bl=blogs.objects.get(id=id)
    context={'bl':bl}
    return render(request,'blogss.html',context)
    
def apply1(request):
    
    gender=request.GET['Gender']
    ms=request.GET['Maritial_status']
    agefrom=request.GET['age']
    ageto=request.GET['age1']
    religion=request.GET['religion']
    education=request.GET['education']
    occupation=request.GET['occupation']
    approval=request.GET['approval']
    data=searchs.objects.filter(Gender=gender,Maritial_status=ms,religion=religion,education=education,occupation=occupation,age__range=[agefrom,ageto],approval=approval)
    
    context={'data':data}
    return render(request,'searchbride.html',context)
    
    
def g(request):
    a=searchs.objects.all()
    context={'a':a}
    return render(request,'searchs.html',context)
    
def homepage(request):
    b=showvideo.objects.all()
    context={'b':b}
    return render(request,'homepage.html',context)


def log(request):
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/login1/')
    else:
        form=loginform()
    return render(request,'registration/sign.html',{'form':form})
        
def serchdetail(request,id):
    sh=serch.objects.get(id=id)
    context={'sh':sh}
    return render(request,'searchdetail.html',context)
            
def happystory(request):
    st=story.objects.all()
    context={'st':st}
    return render(request,'happystories.html',context)
    
def stories(request,id):
    st=story.objects.get(id=id)
    context={'st':st}
    return render(request,'storydetail.html',context)


def slists(request):
    if request.method=="POST":
        uid=request.POST['user']
        form=sform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shortaa',id=uid)
    return render(request,'searchbride.html')



def shortaa(request,id):
    data=searchs.objects.filter(user=id,slist='sort',)

   
    context={'data':data}
    return render(request,'short.html',context)