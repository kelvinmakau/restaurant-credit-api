# restaurant-credit-api

- This is an api for managing a small restaurants debts to its loyal customers
- I am using Django REST Framework for it
- I am using django JWT for authentication
- So far only the customer module is working
- You need to create a user using the django admin page and give the user a role so that you will be able to send requests

Testing the Customer View
Using Postman, use the below endpoints
Get the auth token and input it at the Bearer Token in Postman using the following endpoint:
http://127.0.0.1:8000/api/auth-token

List all customers
GET
http://127.0.0.1:8000/api/customers/

Create a customer
POST
http://127.0.0.1:8000/api/customers/

Retrieve one customer
GET
http://127.0.0.1:8000/api/customers/<id>/

Update a customer
PUT
http://127.0.0.1:8000/api/customers/<id>/

Partial update
PATCH
http://127.0.0.1:8000/api/customers/<id>/

Delete a customer
DELETE
http://127.0.0.1:8000/api/customers/<id>/
