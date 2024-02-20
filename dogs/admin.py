from django.contrib import admin
from dogs.models import Dog, Breed


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'breed',)
    list_filter = ('breed',)
    search_fields = ('name',)