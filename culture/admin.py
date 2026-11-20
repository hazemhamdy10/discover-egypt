
from django.contrib import admin
from .models import Article, Destination, Craft


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'status',
        'created_at',
    )

    list_filter = (
        'category',
        'status',
    )

    search_fields = (
        'title',
        'summary',
        'content',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'governorate',
        'created_at',
    )

    search_fields = (
        'name',
        'governorate',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'origin',
    )

    list_filter = (
        'category',
    )

    search_fields = (
        'name',
        'origin',
        'description',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }
