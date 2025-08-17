from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Meal, Order, Payment, User
from . serializers import CustomerSerializer
from .permissions import IsAdmin, IsAdminOrWaiter # for authentication with roles
from rest_framework import filters

# Create your views here.
# I am adding viewsets for the serializers so that I can send and retrieve data with the API
class CustomerViewSet(viewsets.ModelViewSet):
    # Admin or waiter can list, create, retrieve, update
    # Only Admin can delete
    # authentication is required for all operations

    queryset = Customer.objects.all().order_by('-date_created') # Retrieving all customers in order of creation
    serializer_class = CustomerSerializer

    #  I want to implement search anf ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'phone_number', 'email']
    ordering_fields = ['date_created']

    def get_permissions(self):
        # Ensure that user is always authenticated
        base = [IsAuthenticated]

        # Deleting a customer, ADMIN only
        if self.action == 'destroy':
            more = [IsAdmin]

        else:
            # other actions, create, list, update - either the admin or waiter can do it
            more = [IsAdminOrWaiter]

        return [perm() for perm in (base +more)]
