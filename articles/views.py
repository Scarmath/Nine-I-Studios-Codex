# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from articles.models import Article
from django.shortcuts import render_to_response

def index(request):
	latest_articles = Article.objects.all().order_by('-pub_date')[:20]
	return render_to_response('articles/index.html', {	'latest_articles':latest_articles})

def detail(request, article_id):
	requested_article = Article.objects.filter(id=article_id)
	return render_to_response('articles/article.html', {'article':requested_article[0]})


def frontpage(request):
	latest_seven = Article.objects.all().order_by('-pub_date')[:7]
	top_article = latest_seven[:1]
	major_articles = latest_seven[1:3]
	minor_articles = latest_seven[3:]

	return render_to_response('articles/front.html', { 
		'top_article':top_article,
		'major_articles':major_articles,
		'minor_articles':minor_articles,
		})