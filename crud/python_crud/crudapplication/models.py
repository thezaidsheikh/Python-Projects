from django.db import models

# creating a model for our DB.
class Employee(models.Model):
    people = models.Manager()
    eName = models.CharField(max_length=100)
    eEmail = models.EmailField()
    eContact = models.CharField(max_length=15)
    
   # telling to create a table in our python_user DB.
    class Meta:
        db_table="employee"