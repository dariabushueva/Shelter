from django.contrib import admin

from dogs.models import Dog, Category


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


@admin.register(Category)
class DogCategory(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)


