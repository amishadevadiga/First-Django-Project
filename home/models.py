from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.EmailField(max_length = 122)
    phone = models.CharField(max_length = 12)
    desc = models.TextField()
    

    def __str__(self):
        return self.name 

#make migrations means create changes and store in a file
#migrate means apply the pending changes created by migrations

