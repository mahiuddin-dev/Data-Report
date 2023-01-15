from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category.name + " -> " + self.name


class Person(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank= True)
    upozila = models.CharField(max_length=20, null=True, blank= True)
    union = models.CharField(max_length=20, null=True, blank= True)
    village = models.CharField(max_length=20, null=True, blank= True)
    age = models.IntegerField(null=True, blank= True)
    address = models.TextField(null=True, blank= True)



