from django.db import models

class Poorvika(models.Model):
    product_id = models.CharField(max_length=255)
    item_code = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    poorvika = models.CharField(max_length=255)
    flipkart =models.CharField(max_length=255)
    amazon = models.CharField(max_length=255)
    croma = models.CharField(max_length=255)
    reliance = models.CharField(max_length=255)
    vijaysales = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.model_name
    
class HomeApplainces(models.Model):
    item_code = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    Category =  models.CharField(max_length=255)
    Brand =models.CharField(max_length=255)
    Product = models.CharField(max_length=255)
    Poorvika= models.CharField(max_length=255)
    Sathya=models.CharField(max_length=255)
    Vasanth =models.CharField(max_length=255)
    Darling= models.CharField(max_length=255)
    Viveks= models.CharField(max_length=255)
    Croma= models.CharField(max_length=255)
    Amazon= models.CharField(max_length=255)
    Flipkart = models.CharField(max_length=255)
    Reliance = models.CharField(max_length=255)
    Tata_Cliq = models.CharField(max_length=255)
    date = models.DateField()
    def __str__(self):
        return self.model