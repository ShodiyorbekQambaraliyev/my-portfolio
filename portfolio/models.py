from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    insta_link = models.URLField()
    telegram_link = models.URLField()

    def __str__(self):
        return self.name
    
class Home(models.Model):
    fullname = models.CharField(max_length=255)
    darajangiz = models.CharField(max_length=255)
    information_about_yourself = models.CharField(max_length=1000)

    def __str__(self):
        return self.fullname

class Skils(models.Model):
    skils_name = models.CharField(max_length=255)
    skils_logo = models.ImageField(upload_to='skils_logo')

    def __str__(self):
        return self.skils_name