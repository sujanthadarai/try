from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
    

class Product(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=200)
    price=models.FloatField()
    decp=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name




