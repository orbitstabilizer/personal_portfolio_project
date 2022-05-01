from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 250)
    url = models.URLField(blank = True)
    date = models.DateField()
    def __str__(self):
        return self.title
