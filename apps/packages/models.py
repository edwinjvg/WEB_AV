from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['name']
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")    
    def __str__(self):
        return self.name

class Classification(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['name']
        verbose_name = ("Classification")
        verbose_name_plural = ("Classifications")    
    def __str__(self):
        return self.name

        
class Product(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=2000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)  
    assignee = models.ForeignKey(User, null=True,blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(blank = True, upload_to = 'img/')
    
    class Meta:
        ordering = ["-title"]
        permissions = (
        ("can_add_data","can add a new data"),
        )
        
    def __str__(self):
        return self.title

