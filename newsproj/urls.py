from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as ckeditor_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('accounts/',include('accounts.urls')),
    # path('ckeditor', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
