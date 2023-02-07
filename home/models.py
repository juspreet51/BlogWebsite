from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField 

# Create your models here.

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    heading=models.CharField(max_length=70)
    desc=models.TextField()
    # image=models.ImageField(upload_to='category/')
    image=models.CharField(max_length=500,default='https://github.com/dhruvil-shah/BlogWebsite/blob/master/assets/blog1.jpg')
    date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.heading
    def save(self, *args, **kwargs):
        self.date = timezone.now()
        super(Category, self).save(*args, **kwargs)

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    url = models.CharField(max_length=100)
    cat = models.ManyToManyField(Category)
    # image = models.ImageField(upload_to='post/')
    image=models.CharField(max_length=500,default='https://github.com/dhruvil-shah/BlogWebsite/blob/master/assets/blog1.jpg')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.date = timezone.now()
        super(Blog, self).save(*args, **kwargs)

class Skills(models.Model):
    name=models.CharField(max_length=100)
    percentage=models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Experience(models.Model):
    timeline=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Project(models.Model):
    title=models.CharField(max_length=100)
    # image=models.ImageField(upload_to='project/')
    image=models.CharField(max_length=500,default='https://github.com/dhruvil-shah/BlogWebsite/blob/master/assets/blog1.jpg')
    github_link=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Personal(models.Model):
    name=models.CharField(max_length=30)
    desc=RichTextField()
    # image = models.ImageField(upload_to='personal/')
    image=models.CharField(max_length=500,default='https://github.com/dhruvil-shah/BlogWebsite/blob/master/assets/blog1.jpg')
    email=models.EmailField()
    github=models.CharField(max_length=200)
    facebook=models.CharField(max_length=200)
    website=models.CharField(max_length=200)
    linkedin=models.CharField(max_length=200)
    twitter=models.CharField(max_length=200,default="")
    youtube=models.CharField(max_length=200,default="")
    phone=models.IntegerField()
    # resume=models.FileField(upload_to='resume/')
    # resume=models.ImageField(upload_to='personal/')
    resume=models.CharField(max_length=500,default='https://github.com/dhruvil-shah/BlogWebsite/blob/be7236d6b47d31dfe6505f1a7ab37d1425d02d81/media/resume/resume.pdf')
    year_experience=models.IntegerField(default=0)
    project_completed=models.IntegerField(default=0)
    happy_client=models.IntegerField(default=0)
    customer_review=models.IntegerField(default=12)
    skills = models.ManyToManyField(Skills)
    experience=models.ManyToManyField(Experience)
    project=models.ManyToManyField(Project)


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    subject=models.CharField(max_length=100)
    query=models.CharField(max_length=1000)



