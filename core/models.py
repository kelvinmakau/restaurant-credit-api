from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
# Models I will be using for my restaurant credit system api app

# Custom user with roles
class User(AbstractUser): 
    phone_number = models.CharField(max_length=15, unique=True, blank=True)  # User phone number
    ROLE_CHOICES = ( # Defining my user roles
        ('ADMIN', 'ADMIN'), # Admin role
        ('WAITER', 'WAITER'), # Waiter role
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES) # User role field
    # date_joined comes from AbstractUser
    # is_active also comes from AbstractUser


    def __str__(self):
        return f"{self.username} - {self.role}" # User and role
    
# Customer
class Customer(models.Model):
    full_name = models.CharField(max_length=100, blank=True) # Customer name
    phone_number = models.CharField(max_length=15, unique=True) # Customer phone number
    email = models.EmailField(blank=True, null=True) # Customer email 
    date_created = models.DateField(auto_now_add=True) # Date when the customer was created

    def __str__(self):
        return self.full_name   
# Meal
class Meal(models.Model):
    name = models.CharField(max_length=100) # Meal name
    description =  models.TextField(blank=True) # Meal description, optional
    price = models.DecimalField(max_digits=10, decimal_places=2) # Meal price
    date_created = models.DateField(auto_now_add=True) # Date when the meal was created

    def __str__(self):
        return f"{self.name} - {self.price}" # Meal name and price
    
# Order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders') # Customer who made the order
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='orders') # Meal ordered
    quantity = models.PositiveIntegerField(default=1) # Quantity of the meal ordered
    total_price = models.DecimalField(max_digits=10, decimal_places=2) # Total price for the order
    date_created = models.DateTimeField(auto_now_add=True) # Order creation time
    is_paid = models.BooleanField(default=False) # Payment status of the order
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders') # User who created the order

    def __str__(self):
        return f"Order {self.id} for {self.meal} by {self.customer.full_name} worth {self.total_price}"
    
# Payment
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('CASH', 'CASH'),
        ('MPESA', 'M-PESA')
        )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments') # Order associated with the payment, customer can pay partially
    amount = models.DecimalField(max_digits=10, decimal_places=2) # Amount paid
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES) # Payment method used
    payment_date = models.DateTimeField(auto_now_add=True) # Payment date

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.amount} for customer {self.order.customer.full_name}"