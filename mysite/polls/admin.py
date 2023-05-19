from django.contrib import admin

from .models import Question

admin.site.register(Question)

# Only one more thing to do: we need to tell the admin that Question objects have an admin interface.