from django.contrib import admin
from .models import Article, Category, News, Reporter

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_at', 'reporter')
    list_filter = ('category', 'reporter')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_at'
    prepopulated_fields = {'title': ('title',), 'title': ('title',)}
    readonly_fields = ('published_at',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('published_at', 'category', 'reporter')
    list_filter = ('category', 'reporter')
    search_fields = ('content',)
    date_hierarchy = 'published_at'
    readonly_fields = ('published_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)   
