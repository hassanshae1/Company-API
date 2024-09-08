from django.db import models

# Create your models here.

#creating Company model
class Company(models.Model):
    company_id =models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ('Mobiles Phone','Mobiles Phone')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name+'--'+ self.location
    
    
#Employee Model creating
class Employee (models.Model):
        id= models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        address = models.CharField(max_length=100)
        phone_no = models.CharField(max_length=11)
        about=models.TextField()
        position=models.CharField(max_length=50,choices=(
            ('Manager','manager'),
            ('Software Development','sd'),
            ('Project Leader','pl')
        ))
        
        company = models.ForeignKey(Company, on_delete=models.CASCADE)
        
        
        
        
    