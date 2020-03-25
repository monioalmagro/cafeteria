from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.model.Admin):
    readonly_fields=('created', 'update')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')
    list_display=('title','author','published')
    ordering = ('author','publishead')
    search_fields = ('title','content','author','author__username','categories__name')
    list_filter = ('author__username','categories__name')
    
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
