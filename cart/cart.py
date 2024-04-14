from django.conf import settings 
from menu.models import Food 
from decimal import Decimal 
from coupon.models import Coupon

class Cart:
    def __init__(self, request):
        self.session = request.session 
        self.coupon_id = self.session.get('coupon_id')
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            
        self.cart = cart 
        
    def add_to_cart(self, food, quantity=1, override_quantity=False):
        food_id = str(food.id)
        if food_id not in self.cart:
            self.cart[food_id] = {'quantity':0, 'price':food.price}
        if override_quantity:
            self.cart[food_id]['quantity'] = quantity 
        else:
            self.cart[food_id]['quantity'] += quantity 
        self.save()
        
        
    def save(self):
        self.session.modified = True 
         
    def remove_from_cart(self, food):
        food_id = str(food.id)
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()   
            
    def __iter__(self):
        food_ids = self.cart.keys()
        foods = Food.objects.filter(id__in=food_ids)  
        
        cart = self.cart.copy()
        for food in foods:
            cart[str(food.id)]['food'] = food 
            
        for item in cart.values():
            item['total_price'] = item['price'] * item['quantity']  
            yield item 
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
         
               
    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass 
        return None 

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal(100)) * self.get_total_price()
        return Decimal(0)

    def get_total_price_after_discount(self):
        return self. get_total_price() - self.get_discount()