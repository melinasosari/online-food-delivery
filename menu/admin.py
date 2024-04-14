from django.contrib import admin
from .models import Category, Food


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    
    
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'ingredients', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    list_editable = ['price']
    prepopulated_fields = {'slug':('name',)}


    

