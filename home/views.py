from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog,Category,Contact,Personal
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from bs4 import BeautifulSoup
from django.core.paginator import Paginator


# Create your views here.

def handler404(request, exception):
    return render(request,'404.html')

def handler500(request):
    return render(request,'500.html')

def home(request):
    categories=Category.objects.all()
    context={"categories":categories,"type":"all"}
    return render(request,'home.html',context=context)

def home_query(request,query):
    queryList = Q()
    query=query.split(",")
    for cat in query:
        queryList = queryList | Q(heading__iexact=cat)
    categories = Category.objects.filter(queryList)
    context={"categories":categories,"type":"selected"}
    return render(request,'home.html',context=context)

def blog(request):
    blog = Blog.objects.all()
    for bg in blog:
        str=bg.content
        length=min(250,len(str))
        str=str[0:length]+"..."
        bg.content=str
    context={"blogs":blog,"type":"all"}
    return render(request,'blog.html',context)

def blog_tag(request,tag):
    blogs=Blog.objects.all()
    blog=[]
    for bg in blogs:
        for cate in bg.cat.all():
            catt="{}".format(cate)
            if catt==tag:
                blog.append(bg)
                break
    for bg in blog:
        str=bg.content
        length=min(250,len(str))
        str=str[0:length]+"..."
        bg.content=str
    context={"blogs":blog,"type":"all"}
    return render(request,'blog.html',context)

def about(request):
    personal=Personal.objects.all()
    context={"perabt":personal}
    return render(request,'about.html',context)

def category(request,tag):
    categories=Category.objects.filter(heading__iexact=tag)
    category={}
    for cat in categories:
        category["heading"]=cat.heading
        category["desc"]=cat.desc
        category["image"]=cat.image
        category["date"]=cat.date
    blogs=Blog.objects.all()
    blog=[]
    for bg in blogs:
        for cate in bg.cat.all():
            catt="{}".format(cate)
            if catt==tag:
                blog.append(bg)
                break
    for bg in blog:
        str=bg.content
        length=min(100,len(str))
        str=str[0:length]+"..."
        bg.content=str
    return render(request,"category.html",{"category":category,"blog":blog})

@csrf_protect
def contact(request):
    print("Hii")
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        query =request.POST['query']
        contact=Contact(name=name, email=email, phone=phone,subject=subject,query=query)
        contact.save()
        context={"name":name}
    return render(request,'contact.html',context)

def blog_title(request,title):
    blogid=Blog.objects.get(title=title)
    return render(request,'showblog.html',{"blogid":blogid})


def blog_all(request,page):
    Blogs=Blog.objects.all()
    paginator=Paginator(Blogs,3)
    page_number=page
    BlogsFinalData=paginator.get_page(page_number)
    totalPage=BlogsFinalData.paginator.num_pages
    pageList=[n+1 for n in range(totalPage)]
    return render(request,'showmore.html',{"blogData":BlogsFinalData,"pageList":pageList,"currPage":page_number})

def search(request):
    title=request.GET['query-title']
    searchBlogs=Blog.objects.filter(title__icontains=title)
    return render(request,'searchBlogs.html',{"searchBlog":searchBlogs})

    
