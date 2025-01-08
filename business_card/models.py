from django.db import models
from django.contrib.auth.models import User
import uuid

class BusinessCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # Main details
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    #social media
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkdin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    reddit = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    
    # Media files
    company_logo = models.ImageField(upload_to='logos/')
    profile_image = models.ImageField(upload_to='profiles/')
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    
    # Customizable colors
    primary_color = models.CharField(max_length=7, default="#701B98")  # Background of the entire card
    seconday_color = models.CharField(max_length=7, default="#9E0505")  # Background of the details box

    def __str__(self):
        return self.name + " " + str(self.unique_id)

