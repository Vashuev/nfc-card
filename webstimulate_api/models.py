from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    comment = models.TextField()

    def __str__(self):
        return self.name
