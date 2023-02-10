from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
class subcategory(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name +"->"+  self.category.name

class audiofile(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='audio/images/')
    author = models.CharField(max_length=100)
    discription = models.TextField()
    tags = models.TextField()
    price = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/audiofiles/')

    def __str__(self):
        return self.title