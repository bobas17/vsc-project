from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    plan = models.CharField(max_length=50)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

class Complaint(models.Model):
    customer_name = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.customer_name
