from string import punctuation
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    python_skill = models.IntegerField(default=0)
    sql_skill = models.IntegerField(default=0)
    java_skill = models.IntegerField(default=0)
    spark_skill = models.IntegerField(default=0)
    html_css_skill = models.IntegerField(default=0)

    def __str__(self):
        return self.username