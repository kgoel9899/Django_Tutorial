from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

# python manage.py runserver 8080 - to change the port
# python manage.py runserver 0.0.0.0:8000 - to change the IP

# The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file.