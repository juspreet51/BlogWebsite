from home.models import Blog,Category,Contact,Personal,Skills,Project,Experience
import datetime
from django.db.models import Q

def getLinks(request):
    personal=Personal.objects.first()
    return{'personal':personal}


def getCategory(request):
    category=Category.objects.all()    
    return{'category':category}

def getYear(request):
    today = datetime.date.today()
    year = today.strftime("%Y")
    return {"year":year}

def getBlog(request):
    blog = Blog.objects.all().order_by('-date')[:5]
    for bg in blog:
        str=bg.content
        length=min(250,len(str))
        str=str[0:length]+"..."
        bg.content=str
    return{'blog':blog}

def getBlogAll(request):
    blog = Blog.objects.all().order_by('-date')
    for bg in blog:
        str=bg.content
        length=min(250,len(str))
        str=str[0:length]+"..."
        bg.content=str
    return{'blogs':blog}

def getSkills(request):
    skill=Skills.objects.all()
    return{'skill':skill}

def getProject(request):
    project=Project.objects.all()
    return{'project':project}

def getExperience(request):
    experience=Experience.objects.all()
    return{'experience':experience}
    

