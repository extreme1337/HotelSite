from django.db import models

property_type = (
    ("Sale", "sale"),
    ("Rent", "rent")
)

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=property_type)
    price = models.FloatField()
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    area = models.FloatField()
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
    

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='property/category/')


    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name
    

