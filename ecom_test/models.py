from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    product_title = models.CharField(max_length=100)
    product_image = models.ImageField(default='default.jpg', upload_to='product_images')
    product_desc = models.TextField()
    product_price = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_title

    def get_absolute_url(self):
        #return reverse('home')
        return reverse('product-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.product_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.product_image.path)