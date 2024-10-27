from modeltranslation.translator import register, TranslationOptions
from .models import Category, Article, News

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('content',)
