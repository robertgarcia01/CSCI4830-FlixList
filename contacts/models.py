from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    watches = models.CharField(max_length=2)

    def __str__(self):
        return self.name
