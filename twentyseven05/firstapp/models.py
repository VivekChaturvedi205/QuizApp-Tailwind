from django.db import models

class students(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=265)
    age=models.IntegerField(default=18)
    createdAt=models.DateTimeField(auto_now=True)
    deletedAtp=models.DateTimeField(null=True, blank=True)
    updatedAt=models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name