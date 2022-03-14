from django.db import models

# Create your models here.
class Owners(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'
    
    def __str__(self):
        return self.name


class Dogs(models.Model):
    owner = models.ForeignKey('Owners', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    age = models.IntegerField()

    class Meta:
        db_table = 'dogs'
    
    def __str__(self):
        return self.name
