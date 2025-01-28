from django.db import models

# Create your models here.
class movies(models.Model):
    
    movie_name=models.CharField(max_length=100,default="")
    release_date=models.DateField()
    category=models.CharField(max_length=50)
    language=models.CharField(max_length=10)
    description=models.CharField(max_length=30,default="")
    image=models.ImageField(upload_to="movies/images",default="")


    def __str__(self) -> str:
        return self.movie_name

