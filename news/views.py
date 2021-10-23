from django.shortcuts import redirect, render
from .form import article_form
from .models import News,Category,Trend,Banner
from accounts.models import author
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    x = Category.objects.all()
    y = Trend.objects.all()
    z = Banner.objects.all()
    all_news = News.objects.all()
    context = {"cat":x,"trend":y,"new":y,"all_new":all_news}
    return render(request,'index.html',context)

def add_article_page(request):
    form = article_form()
    context = {"form":form}
    return render(request,'news/add_article.html',context)


@login_required(login_url='accounts/login_page')
def save_article(request):
    if request.method == "POST":
        current_user = request.user
        print(f"current_user is {current_user}")
        auth = author.objects.get(user = current_user)
        title = request.POST.get('title')
        category = request.POST.get('category')
        print(f"category  is {category}")
        cat = Category.objects.get(id = category)
        main_img = request.FILES.get('main_image')
        main_img_url = request.POST.get('main_image_url')
        body = request.POST.get('body')
        meta_title = request.POST.get('meta_title')
        meta_keyword = request.POST.get('meta_keyword')
        # tags = request.POST.get('tags')
        x = News.objects.create(title = title,category = cat,main_image = main_img,main_image_url = main_img_url,body = body,meta_title = meta_title,meta_keyword = meta_keyword,writer = auth)
        x.save()
        messages.info(request,"The Article has been succesfully created")
        return redirect('news/add_article')
    else:
        messages.info(request,"Article Cant be Added")
        return redirect('/news/add_article')

def article_detail(request,id):
    z = Category.objects.all()
    new = News.objects.get(id = id)
    context = {"new":new,"cat":z}
    return render(request,"news/article_detail.html",context)

def news_cat(request,id):
    z = Category.objects.all()
    cat_obj = Category.objects.get(id= id)
    x = News.objects.filter(category = cat_obj)
    context = {"all_new":x,"cat":z}
    return render(request,"news/category_news.html",context)

         