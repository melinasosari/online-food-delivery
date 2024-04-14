from django.db import models
from menu.models import Food 

class Order(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField()
    address = models.TextField()
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return f"order {self.id}"
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='order_items', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity

    

  