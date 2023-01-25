from django.contrib import admin
from .models import Category,Blog,Contact,Personal ,Experience,Skills,Project
#

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):    
    search_fields = ('heading',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 20

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone')
    search_fields = ('name','email')
    list_per_page = 20

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Personal)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Project)
