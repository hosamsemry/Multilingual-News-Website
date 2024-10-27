from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.utils import translation
from .models import Article, News, Category

# Home Page View
class HomeView(ListView):
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # Fetch all articles considering the current language.
        language = translation.get_language()
        return Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.get_queryset()
        context['news_items'] = News.objects.all()
        
        # Prepare categories with translations.
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'news_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context


class CategoryView(ListView):
    template_name = 'news/category.html'
    context_object_name = 'news'

    def get_queryset(self):
        # Get the news items filtered by category.
        category_id = self.kwargs['category_id']
        return News.objects.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        
        # Get the selected category.
        context['category'] = Category.objects.get(pk=category_id)
        
        # Get all news items for the selected category.
        context['news'] = self.get_queryset()
        
        # Get all articles for the selected category.
        context['articles'] = Article.objects.filter(category_id=category_id)
        
        # Optionally, get all categories for the sidebar or navigation.
        context['categories'] = [(category, category.name) for category in Category.objects.all()]

        return context


class AboutView(TemplateView):
    template_name = 'news/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context


class ContactView(TemplateView):
    template_name = 'news/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'content', 'category', 'image']
    template_name = 'news/article_update.html'
    permission_required = 'news.can_update_article'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Adding CSS classes directly to the form fields
        form.fields['title'].widget.attrs['class'] = 'form-control'
        form.fields['content'].widget.attrs['class'] = 'form-control'
        form.fields['category'].widget.attrs['class'] = 'form-select'
        form.fields['image'].widget.attrs['class'] = 'form-control'  # For file input
        return form


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = 'news/article_confirm_delete.html'
    permission_required = 'news.can_delete_article'
    success_url = reverse_lazy('news:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = News
    fields = ['content', 'category', 'image']
    template_name = 'news/news_update.html'
    permission_required = 'news.can_update_news'
    context_object_name = 'news_item'

    def get_success_url(self):
        return reverse('news:news_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Adding CSS classes directly to the form fields
        form.fields['content'].widget.attrs['class'] = 'form-control'
        form.fields['category'].widget.attrs['class'] = 'form-select'
        form.fields['image'].widget.attrs['class'] = 'form-control'  # For file input
        return form


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    permission_required = 'news.can_delete_news'
    success_url = reverse_lazy('news:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [(category, category.name) for category in Category.objects.all()]
        return context
