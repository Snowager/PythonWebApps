from django.contrib import admin
from .models import Hero, Author

# Register your models here.
admin.site.register(Author)
admin.site.register(Hero)