from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from io import BytesIO
from PIL import Image

from django.core.files import File

from django_resized import ResizedImageField





# Create your models here.




class NewsModel(models.Model):
    title =  models.CharField(max_length=255 , unique=True)
    descripton = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    price = models.IntegerField(null=True, blank=True )

    image = models.ImageField( upload_to='images/',
        verbose_name=_("Main Photo"), default="", null=True, blank=True , 
    )
    thumbnail = ResizedImageField(size=[300, 200], quality=85 , default='348133-sekogash-imate-izbor.jpg')
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

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return f'/{self.slug}/'

   


    def get_image(self):
        if self.image:
            print("sjdnjsdcnjcdsjcns")
            return 'http://127.0.0.1:8000' + self.image.url
            print(self.image.url)
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
       
        else:
            return ''
    
    