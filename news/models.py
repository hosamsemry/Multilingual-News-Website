from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Category(models.Model):
    name= models.CharField(_("name"), max_length=100, )

    def __str__(self):
        return self.name


class Reporter(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    # Store content in different languages using a translation library or custom logic
    content = models.TextField(_("Content"))
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, verbose_name=_("Reporter"))
    published_at = models.DateTimeField(_("Published At"), auto_now_add=True)
    image = models.ImageField(upload_to='news/', verbose_name=_("Image"), default='news/default.png')

    def __str__(self):
        return f"{self.published_at.strftime('%Y-%m-%d')}"

    def get_absolute_url(self):
        return reverse('news:news_detail', kwargs={'pk': self.pk})

class Article(models.Model):
    title = models.CharField(_("Title"),max_length=200,)
    content = models.TextField(_("Content"))
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    reporter = models.ForeignKey(Reporter, verbose_name=_("Reporter"), on_delete=models.CASCADE)
    published_at = models.DateTimeField(_("Published At"), auto_now_add=True)
    image = models.ImageField(upload_to='articles/', verbose_name=_("Image"), default='articles/default.png')

    def __str__(self):
        return self.title  
    
    def get_absolute_url(self):
        return reverse('news:article_detail', kwargs={'pk': self.pk})
