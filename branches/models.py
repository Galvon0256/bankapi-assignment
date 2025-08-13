from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.branch} ({self.ifsc})"
