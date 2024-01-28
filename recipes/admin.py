from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import format_html

from .models import Recipe, Product, RecipeProductItem


class RecipeProductItemInline(admin.TabularInline):
    model = RecipeProductItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'get_image_list_preview',
        'name',
    ]

    list_filter = [
        'name',
    ]

    inlines = [
        RecipeProductItemInline
    ]

    readonly_fields = [
        'get_image_preview',
    ]

    def get_image_preview(self, obj):
        if not obj.image:
            return 'выберите картинку'
        return format_html('<img src="{url}" style="max-height: 200px;"/>', url=obj.image.url)
    get_image_preview.short_description = 'превью'

    def get_image_list_preview(self, obj):
        if not obj.image or not obj.id:
            return 'нет картинки'
        edit_url = reverse('admin:recipes_recipe_change', args=(obj.id,))
        return format_html('<a href="{edit_url}"><img src="{src}" style="max-height: 50px;"/></a>', edit_url=edit_url, src=obj.image.url)
    get_image_list_preview.short_description = 'превью'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'number_of_uses',
    ]

    list_filter = [
        'name',
        'number_of_uses',
    ]

    search_fields = [
        'name',
        'number_of_uses',
    ]

    inlines = [
        RecipeProductItemInline
    ]


@admin.register(RecipeProductItem)
class RecipeProductItemAdmin(admin.ModelAdmin):
    list_display = [
        'recipe',
        'product',
        'weight',
    ]

    list_filter = [
        'recipe',
        'product',
        'weight',
    ]