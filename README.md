# restaurant-credit-api

- A RESTFful API made with Django REST Framework for managing a restaurants debt operations
- It allows managing of users, customers, meals, orders and payments
- It enforces permissions and data integrity

## Features

- User Management - create, list, update, delete
- Customer Management - Store customer details, track credit orders
- Meal Management - Menu items with name, description and price
- Order Management - Create customer orders, autocalculate totals, assign order creator
- Payment Management - Track payments per order and automatically update the payment status
- Role-based permissions - Control who can create, delete or update e.g. Admins are the only ones who can delete
- Timestamps for tracking order and payment history

## Tech Stack

- Python 3.11
- Django 5.0.4
- Django RESTFramework
- Django simple JWT
- SQlite - default but can be reconfigured to MySQL, POSTGRES etc

## Project Structure

restaurant_credit/ # root folder

|--- core/ # Main app, handles every model users, customers, payments, orders and meals

|--- restaurant_credit/ # Project settings and urls

|--- manage.py

|--- db.sqlite3

|--- README.md

|--- requirements.txt

## Installation

1. Clone this repo:
git clone `https://github.com/kelvinmakau/restaurant-credit-api.git`

2. Create a virtual envrionment(optional but recommended) and activate it

    On Windows

    - `cd restaurant-credit-api` - Open terminal/command prompt in the project folder

    - `python -m venv myvenv` - Create the virtual environment

    - `myenv\Scripts\activate` - Activate your environment

    On Linux/Mac

    - `cd restaurant-credit-api` - Open terminal/command prompt in the project folder

    - `python -m venv myvenv` - Create the virtual environment

    - `source myenv/bin/activate` - Activate your environment

3. Install the dependencies, required modules
`pip install -r requirements.txt`

4. Run migrations
`python manage.py migrate`

5. Create superuser
`python manage.py createsuperuser`

6. Run the server
`python manage.py runserver`

- If you don't change the port, it should run at `http://127.0.0.1:8000/api/`

## API Endpoints

### Users

POST /api/users/ → Create user

sample data

``` json
{
    "username": "kelia",
    "password": "1234",
    "email": "kelia@kelly.com",
    "role": "WAITER",
    "phone_number": "0708010107",
    "is_staff": true,
    "is_superuser": false
}
```

Only set is_staff = true if you want the user to be able to access the admin page

GET /api/users/ → List users

sample response

```json
{
    "id": 8,
    "username": "kelia",
    "email": "kelia@kelly.com",
    "role": "WAITER",
    "phone_number": "0708010107",
    "is_staff": true,
    "is_superuser": false
}
```

### Customers

POST /api/customers/ → Create customer

sample data

``` json
{

  "full_name": "Jane Mafia",
  "phone_number": "0722000000",
  "email": "jane@gmail.com"

}

```

GET /api/customers/ → List customers

```json
{
    "id": 5,
    "full_name": "Jane Mafia",
    "phone_number": "0722000000",
    "email": "jane@gmail.com",
    "date_created": "2025-08-22",
    "total_paid": "2100.00",
    "total_unpaid": null
}
```

### Meals

POST /api/meals/ → Add meal

sample data

``` json
{
    "name": "Rice chicken",
    "description": "Just rice",
    "price": "200.00"
}
```

GET /api/meals/ → List meals

sample response

``` json
{
    "id": 3,
    "name": "Rice chicken",
    "description": "Just rice",
    "price": "200.00",
    "date_created": "2025-08-28"
}
```

### Orders

POST /api/orders/ → Create order (auto-calculates total)

sample data

```json
{
  "customer": 5,
  "meal": 3,
  "quantity": 1
}
```

GET /api/orders/ → List orders

sample response

```json
{
    "id": 6,
    "customer": 5,
    "customer_name": "Jane Mafia",
    "meal": 3,
    "meal_name": "Rice chicken",
    "quantity": 1,
    "total_price": "200.00",
    "date_created": "2025-08-28T13:52:51.053763+03:00",
    "is_paid": false,
    "created_by": 1,
    "user_name": "admin"
}
```

### Payments

POST /api/payments/ → Make payment (auto-updates order’s is_paid)

sample data

```json
{
  "order": 6,
  "amount": 200.00,
  "payment_method": "MPESA"
}
```

GET /api/payments/ → List payments

sample response

```json
{
    "id": 8,
    "order": 6,
    "meal_name": "Rice chicken",
    "amount": "200.00",
    "payment_method": "MPESA",
    "payment_date": "2025-08-28T13:56:21.152986+03:00",
    "customer_name": "Jane Mafia",
    "processed_by": "admin"
}
```

#### DELETING AND GETTING SINGLE OBJECTS

- If you want to delete or retrieve an object(customer, user, meal, order, payment), append the id to the specific object at the end of a url

for instance:

- GET /api/orders/1/ - Retrieves order with id 1

- DELETE /api/orders/1/ - Deletes order with id 1

## Search and Ordering

### Search URLS

`?search=<term>`

Customers View

- `/customers/?search=` - Input search criteria, either name, email or phone number

Meals

- `/meals/?search=` - Input search criteria, name

Orders

- `/orders/?search=` - Input search criteria, customer name, if order is paid(True, False), meal name

Payments

- `/payments/?search=` - Input the search criteria, customer name

Ordering URLS

- Can order by either ascending or descending order

o `?ordering=<field>` - ascending order
o `?ordering=-<field>` - descending order

## Testing the Customer View

Using Postman, use the below endpoints

Get the auth token and input it at the Bearer Token in Postman using the following endpoint:
`http://127.0.0.1:8000/api/auth-token`

- List all customers

GET

`http://127.0.0.1:8000/api/customers/`

- Create a customer

POST

`http://127.0.0.1:8000/api/customers/`

- Retrieve one customer

GET

`http://127.0.0.1:8000/api/customers/<id>/`

- Update a customer

PUT

`http://127.0.0.1:8000/api/customers/<id>/`

- Partial update

PATCH

`http://127.0.0.1:8000/api/customers/<id>/`

- Delete a customer

DELETE

`http://127.0.0.1:8000/api/customers/<id>/`
