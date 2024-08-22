from django.db import models

# Create your models here.
class Movies(models.Model):
    # by  default, when you query this model, it will returns an "object", if you want a different behavior, for example the name of the movie, Do as follows:
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    rating = models.FloatField()
    