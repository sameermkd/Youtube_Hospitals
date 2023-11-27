from django.db import models

class Department(models.Model):
    dep_name=models.TextField(max_length=50)
    dep_desc=models.TextField(max_length=200)
    def __str__(self):
        return self.dep_name
class Doctor(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctores/')
    def __str__(self):
        return self.doc_name
