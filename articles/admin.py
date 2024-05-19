
# Register your models here.
from django.contrib import admin
from .models import Article, Comment  # new

admin.site.register(Article)
admin.site.register(Comment)  # new
