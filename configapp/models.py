from django.db import models

class BaseModel(models.Model):
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Actor(BaseModel):
    name = models.CharField(max_length=150)
    birthdate = models.DateField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.name


class Movie(BaseModel):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    imdb = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    genre = models.CharField(max_length=50, )
    actor = models.ManyToManyField('Actor')

    def __str__(self):
        return self.name