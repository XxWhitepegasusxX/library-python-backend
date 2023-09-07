from django.contrib import admin
from .models import Author, Book, Category
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('author',)

class AuthorAdmin(admin.ModelAdmin):
    filter_horizontal = ('books',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)