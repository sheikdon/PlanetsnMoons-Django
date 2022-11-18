from django.db import models

# Create your models here.
class Outer(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} is {self.size} long!"

    def as_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'size': self.size,

        }