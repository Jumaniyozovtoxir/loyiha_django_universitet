from django.db import models

# Create your models here.

class Guruhlar(models.Model):
    nomi= models.CharField(max_length=50)
    def __str__(self):
        return self.nomi



class Kursantlar(models.Model):
    ism= models.CharField(max_length=400)
    familiya= models.CharField(max_length=400)
    guruh = models.ForeignKey(Guruhlar,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}  {self.familiya}"
