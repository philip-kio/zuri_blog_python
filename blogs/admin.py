from django.contrib import admin
from .models import post, Comment
# Register your models here.



class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline,
    ]

admin.site.register(post,PostAdmin)

admin.site.register(Comment)