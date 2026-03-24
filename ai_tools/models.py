from django.db import models

# Create your models here.
class Trending(models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating_choices=[
        (1,'1 Star'),
        (2,'2 Star'),
        (3,'3 Star'),
        (4,'4 Star'),
        (5,'5 Star'),
    ]
    rating=models.IntegerField(choices=rating_choices)
    url=models.URLField(max_length=200,blank=True)

class Frontend_AI (models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    url=models.URLField(max_length=200,blank=True,null=True)

class Backend_AI (models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    url=models.URLField(max_length=200,blank=True,null=True)

class Database_AI (models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    url=models.URLField(max_length=200,blank=True,null=True)

class AI_chatbot (models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    url=models.URLField(max_length=200,blank=True,null=True)

class Code_generation (models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    url=models.URLField(max_length=200,blank=True,null=True)

class  UI_UX_Design (models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    url=models.URLField(max_length=200,blank=True,null=True)

class Devops_Deployment (models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    url=models.URLField(max_length=200,blank=True,null=True)

class Testing_Security (models.Model):
    img=models.ImageField(upload_to='img/', blank=True, null=True)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    pricing_choices=[
        ("Free","Free"),
        ("Paid","Paid"),
        ("Freemium","Freemium"),
    ]
    pricing=models.CharField(choices=pricing_choices)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    url=models.URLField(max_length=200,blank=True,null=True)