# LibraryProject

A Django web application project for managing library resources.

## Project Overview

This is a Django project created as part of learning Django fundamentals. The project serves as a foundation for developing Django applications with a focus on library management.

## Project Structure

```
LibraryProject/
├── LibraryProject/          # Main project configuration directory
│   ├── __init__.py         # Python package marker
│   ├── settings.py         # Project settings and configuration
│   ├── urls.py            # Main URL configuration (URL dispatcher)
│   ├── wsgi.py            # WSGI application entry point
│   └── asgi.py            # ASGI application entry point
├── manage.py               # Django command-line utility
└── README.md               # This file
```

## Key Components

### settings.py
- Contains all project configuration settings
- Database configuration
- Installed applications
- Middleware settings
- Static files configuration
- Security settings

### urls.py
- Main URL configuration file
- Defines URL patterns and routing
- Acts as a "table of contents" for the Django-powered site

### manage.py
- Command-line utility for interacting with the Django project
- Used for running the development server, creating apps, migrations, etc.

## Getting Started

### Prerequisites
- Python 3.11.3 or higher
- Django 5.2.5

### Running the Development Server

1. Navigate to the project directory:
   ```bash
   cd LibraryProject
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

3. Open your web browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

4. You should see the default Django welcome page.

## Development Workflow

1. **Create Apps**: Use `python manage.py startapp <app_name>` to create new Django applications
2. **Run Migrations**: Use `python manage.py migrate` to apply database changes
3. **Create Superuser**: Use `python manage.py createsuperuser` to create an admin user
4. **Collect Static Files**: Use `python manage.py collectstatic` for production deployment

## Next Steps

- Create Django applications for specific functionality
- Define models for data structure
- Create views and templates
- Configure URL routing for your applications
- Set up database models and migrations

## Django Version

This project uses Django 5.2.5, which includes:
- Modern Python 3.11+ support
- Enhanced security features
- Improved performance
- Latest Django best practices

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/misc/api-stability/)
