from django.urls import path
from news import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add_article',views.add_article_page,name='add_article_page'),
    path('save_article',views.save_article,name='save_article'),
    path('news_cat/<int:id>',views.news_cat,name='news_cat'),
    path('article_detail/<int:id>',views.article_detail,name='article_detail'),

]
