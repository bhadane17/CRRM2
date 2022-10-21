from django.db import models

# Create your models here.
class Weight_distribution(models.Model):
    Filter_Number=models.IntegerField()
    Risk_Assesment=models.CharField(max_length=35)
    Description=models.CharField(max_length=250)
    Weight=models.IntegerField()
    Assesment_Score=models.IntegerField()

class Customer_Type(models.Model):
    Customer_Category=models.CharField(max_length=65)
    Entity_Type=models.CharField(max_length=3)
    High=models.CharField(max_length=4,default='NA')
    Medium=models.CharField(max_length=6,default='NA')
    Low=models.CharField(max_length=4,default='NA')
    Score=models.IntegerField()

class Product_Service(models.Model):
    Product=models.CharField(max_length=48)
    High=models.CharField(max_length=4,default='NA')
    Medium=models.CharField(max_length=6,default='NA')
    Low=models.CharField(max_length=4,default='NA')
    Score=models.IntegerField()

class Juridictional_Risk(models.Model):
    Country_Juridiction=models.CharField(max_length=21)
    High_Risk=models.CharField(max_length=22,default='NA')
    Medium=models.CharField(max_length=6,default='Y')
    Low=models.CharField(max_length=4,default='NA')
    Score=models.IntegerField()

class List_Matching(models.Model):
    List_Name=models.CharField(max_length=62)
    Very_High=models.IntegerField()
    High=models.IntegerField()
    Medium=models.IntegerField()

class Profile_linkage(models.Model):
    Parameters=models.CharField(max_length=134)
    High=models.CharField(max_length=4)
    Medium=models.CharField(max_length=6)
    Low=models.CharField(max_length=4)
    Score=models.IntegerField()

class Transaction_Behavior(models.Model):
    Transaction=models.CharField(max_length=212)
    Frquency_one=models.IntegerField(default='1')
    Score_one=models.IntegerField()
    Frquency_Two=models.IntegerField(default='2')
    Score_two=models.IntegerField()
    Frquency_Three=models.IntegerField(default='3')
    Score_three=models.IntegerField()






