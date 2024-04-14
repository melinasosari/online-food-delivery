from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    
    def get_absolute_url(self):
        return reverse('food_list_by_category', args=[self.slug])
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(Category, related_name='foods', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='media/images', blank=True)
    ingredients = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('food_detail', args=[self.id, self.slug])
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name