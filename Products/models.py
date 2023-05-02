from django.db import models
from PIL import Image

# Create your models here.
class Aksesuar(models.Model):
    name = models.CharField(max_length=100,unique=True)

    
    def __str__(self):
        return str(self.name)
    
class Products(models.Model):
    aksesuarName = models.ForeignKey(Aksesuar, on_delete=models.CASCADE,related_name='aksesuar',to_field='name')
    brandAndType =  models.CharField(max_length=100) 
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20,null=True)
    kalınlık = models.CharField(max_length=20,null=True)
    image= models.ImageField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200)  
    Mat = models.BooleanField(default=False)
    
       
    def __str__(self):
         return str(self.name) 
    
    
    def save (self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 600 or img.width > 600:
                outputs_size = (600,600)
                img.thumbnail(outputs_size)
                img.save(self.image.path)
                
                

                