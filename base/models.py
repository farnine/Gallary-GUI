from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    catagory=models.CharField(max_length=50)
    upload_date=models.DateTimeField(auto_now_add=True)
    upload_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    image_path=models.ImageField(upload_to="images")


    def __str__(self):

        return self.title
