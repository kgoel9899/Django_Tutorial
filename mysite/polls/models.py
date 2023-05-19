import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# models – essentially, your database layout, with additional metadata.

# By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
# this creates polls/migrations/0001_initial.py

# python manage.py sqlmigrate polls 0001 - The sqlmigrate command takes migration names and returns their SQL

# run migrate again to create those model tables in your database

# The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.
# Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:
# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.

# shell -> python manage.py shell
# Question.objects.all()

# Save the object into the database. You have to call save() explicitly.
# q.save()

# q.delete() and so on
# q.choice_set.all() - list of choice for this question

# python manage.py createsuperuser - First we’ll need to create a user who can login to the admin site
