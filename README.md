# Shop Management System

A simple shop management system built using Django. It features product listings, a shopping cart, and customer accounts.

## Features

- **Products**: View product names, prices, stocks, and images.
- **Customers**: Manage customer information, including mobile numbers, emails, and passwords.
- **Shopping Cart**: Add products to a cart and manage quantities associated with specific users.

## Project Structure

- `manage.py`: Django's command-line utility for administrative tasks.
- `app/`: The core Django app containing models.
- `shop/`: The main Django project configuration directory (settings, urls).
- `template/`: HTML templates for the frontend.
- `static/`: Static files like CSS and JS.
- `media/`: Uploaded media files, such as product images.

## Requirements

- Python 3.x
- Django

## Installation & Running

1. Clone or download the repository.
2. Navigate to the project root directory where `manage.py` is located.
3. Install Django (if not already installed):
   ```bash
   pip install django
   ```
4. Run migrations to set up the database (SQLite3 is included by default):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Navigate to `http://127.0.0.1:8000/` in your web browser.
