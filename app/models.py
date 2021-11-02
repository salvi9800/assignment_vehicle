from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to ='uploads', null=True, blank=True)

    def __str__(self):
        return "{title}".format(title=self.name)

class Vehicle(models.Model):
    model = models.PositiveIntegerField(max_length=4)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    speed = models.PositiveIntegerField()
    average_speed = models.PositiveIntegerField()
    temperature = models.FloatField()
    fuel_level = models.CharField(max_length=10)
    engine = models.FloatField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to ='uploads', null=True, blank = True, default='default.png')
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)

    def __str__(self):
        return "{model}-{brand}".format(model=self.model, brand = self.brand)    

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.photo:
                self.thumbnail = self.make_thumbnail(self.photo)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg' 
    
    def make_thumbnail(self, photo, size=(300,200)):
        img = Image.open(photo)
        img.convert('RGB')
        img.thumbnail(size)   #an inbuilt method from PIL

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=photo.name)

        return thumbnail

