from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) 
# so it is like that of route in Flask where that admin stuff is like factory function