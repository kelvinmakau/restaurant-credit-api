from django.contrib import admin
from .models import User, Customer, Meal, Order, Payment

# Register your models here.
admin.site.register(User)  # Registering the custom user model
admin.site.register(Customer)  # Registering the customer model
admin.site.register(Meal)  # Registering the meal model
admin.site.register(Order)  # Registering the order model 
admin.site.register(Payment)  # Registering the payment model
