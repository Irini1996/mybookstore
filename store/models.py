from django.db import models #Import the Django models module.
#This gives you access to all the field types (CharField, DecimalField, TextField, etc.) that you use to define database tables.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2) #A decimal number field, used for money/prices
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #A date & time field  
    #auto_now_add=True → Django will automatically set this field to the current date/time when the record is first created.

    def __str__(self):  #A special Python method that defines the string representation of the object.
        return self.title #With this method, when you print the object, it shows the book’s title instead.
