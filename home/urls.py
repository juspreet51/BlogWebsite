from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.home,name='home'),
    path('blog/blogs',views.blog, name='blog'),
    path('blog/blogs/<int:id>',views.blog_tag, name='blog_tag'),
    path('blog/<str:title>',views.blog_title,name='blog_id'),
    path('about/aboutme',views.about, name='about'),
    path('category/<str:tag>',views.category, name='category'),
    path('contact/contactus',views.contact, name='contact')
    # path('<str:query>/',views.home_query, name='home_query')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
