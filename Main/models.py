from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100,verbose_name='Blog\'s title')
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    body=models.TextField(verbose_name='Blog\'s body')
    def __str__(self):
        return self.title