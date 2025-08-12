from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Models I will be using for my restaurant credit system api app

# Custom user with roles
class User(AbstractUser): 
    ROLE_CHOICES = ( # Defining my user roles
        ('ADMIN', 'admin'),
        ('WAITER', 'waiter')
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES) # User role field


    def __str__(self):
        return f"{self.username} - {self.role}" # User and role
    
# Customer
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')  
    phone_number = models.CharField(max_length=15, unique=True) 

    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
# Meal
class Meal(models.Model):
    name = models.CharField(max_length=100) # Meal name
    description =  models.TextField() # Meal description
    price = models.DecimalField(max_digits=10, decimal_places=2) # Meal price

    def __str__(self):
        return self.name
    
# Order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders') # Customer who made the order
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='orders') # Meal ordered
    quantity = models.PositiveIntegerField(default=1) # Quantity of the meal ordered
    total_price = models.DecimalField(max_digits=10, decimal_places=2) # Total price for the order
    created_at = models.DateTimeField(auto_now_add=True) # Order creation time

    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username}"
    
# Payment
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('CASH', 'Cash'),
        ('MPESA', 'M-Pesa')
        )

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment') # Order associated with the payment
    amount = models.DecimalField(max_digits=10, decimal_places=2) # Amount paid
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES) # Payment method used
    payment_date = models.DateTimeField(auto_now_add=True) # Payment date

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.amount}"