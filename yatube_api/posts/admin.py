from django.contrib import admin

from .models import Comment, Group, Post


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    title = ('text',)
    slug = ('pk', 'text',)
    description = ('text',)
    empty_value_display = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('group',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'text',
        'created',
        'author',
    )
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'
