from django.contrib import admin
from .models import Video, Category


@admin.register(Video)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'published')
    #prepopulated_fields = ()
    
admin.site.register(Category)