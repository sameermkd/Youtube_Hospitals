from django.db import models

class Department(models.Model):
    dep_name=models.TextField(max_length=50)
    dep_desc=models.TextField(max_length=200)
    def __str__(self):
        return self.dep_name
