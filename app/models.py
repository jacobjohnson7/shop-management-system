from django.db import models

class product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.product_name} - {self.price}- {self.stock}- {self.image}"
    
class customer(models.Model):
    firstname=models.CharField(max_length=50)
    mobile=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=128)
   
class Cart(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(customer, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()


    