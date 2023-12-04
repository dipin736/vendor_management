

# Vendor Management System

## Introduction

The Vendor Management System, developed using Django, is a web application designed for streamlined vendor relationship management. 

It encompasses functionalities for managing vendor profiles, tracking purchase orders, and evaluating vendor performance. 

Users can create, update, and delete vendor profiles, monitor purchase orders, and assess vendor performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate. 

## Features

- User/Admin can add or remove vendors 
- Vendors can see the list of different members
- Admin can give the perfect calculations for performance
- Easy to use
- API endpoints can be checked using Django ORM
- No need of any tools is needed for API endpoints checking.


## API Reference

#### Vendor Profile Management:

```http
  POST /api/vendors/: Create a new vendor.
  GET /api/vendors/: List all vendors.
  GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
  PUT /api/vendors/{vendor_id}/: Update a vendor's details.
  DELETE /api/vendors/{vendor_id}/: Delete a vendor.
```


#### Purchase Order Tracking:

```http
  POST /api/purchase_orders/: Create a purchase order.
  GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
  GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
  PUT /api/purchase_orders/{po_id}/: Update a purchase order.
  DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
```


#### Historical Performance:

```http
  GET /api/vendors/{vendor_id}/performance
```

## Tech Stack

**Stack:** Python, Django, dbsqlite3

**Server:** localhost:8000


## Installation

```bash
python -m venv venv

source venv/Scripts/activate

pip install django

pip install djangorestframework

pip install -r requirements.txt

python manage.py makemigrations 

python manage.py migrate

python manage.py createsuperuser 

python manage.py runserver

http://localhost:8000/vendors/  --for vendor list

http://localhost:8000/admin  --for admin




