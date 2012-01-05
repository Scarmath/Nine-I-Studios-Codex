#admin.py
#--------
#Admin for the Article model

from articles.models import Article
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
	fields = ['title','byline', 'pub_date','body']

admin.site.register(Article, ArticleAdmin)