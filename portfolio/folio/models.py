from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_name=models.CharField(max_length=50)
    contact_email=models.EmailField(max_length=254)
    contact_phone=models.CharField(max_length=12)
    contact_message=models.TextField(blank=True)

    def __str__(self):
        return self.contact_name