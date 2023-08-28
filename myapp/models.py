from django.db import models

class AppBar(models.Model):
    home = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    wines = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return "AppBar"
    
class Portell(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default="N/A")
    alcohol = models.CharField(max_length=50, default="N/A" )
    variety = models.CharField(max_length=255, default="N/A")
    description = models.TextField()
    image = models.ImageField(upload_to='wines/', blank=True, null=True)

    def __str__(self):
        return "Portell"
    
class Landing(models.Model):
    text = models.CharField(max_length=255)
    description = models.TextField()
    caption = models.CharField(max_length=255)
    button = models.CharField(max_length=255)

    def __str__(self):
        return "Landing"
    
class Message(models.Model):
   first = models.CharField(max_length=255)
   second = models.CharField(max_length=255)
   third = models.CharField(max_length=255)
   fourth = models.CharField(max_length=255)
   
   def __str__(self):
        return "Message"


class Body(models.Model):
    text = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "Body"


class Contact(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "Contact"

