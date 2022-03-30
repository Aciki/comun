from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.




class NewsModel(models.Model):
    title =  models.CharField(max_length=255,blank = True, null = True)
    descripton = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    cover_photo = models.ImageField(
        verbose_name=_("Main Photo"), default="", null=True, blank=True
    )
    photo1 = models.ImageField(
        
        null=True,
        blank=True,
    )
    photo2 = models.ImageField(
       
        null=True,
        blank=True,
    )
    photo3 = models.ImageField(
        
        null=True,
        blank=True,
    )
    photo4 = models.ImageField(
        
        null=True,
        blank=True,
    )