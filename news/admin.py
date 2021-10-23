from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Trend)
admin.site.register(Banner)
