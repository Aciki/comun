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

    image = models.ImageField(
        verbose_name=_("Main Photo"), default="", null=True, blank=True
    )
    thumbnail = ResizedImageField(size=[300, 200], quality=85)
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

   


    # def get_image(self):
    #     if self.image:
    #         print("sjdnjsdcnjcdsjcns")
    #         return 'http://127.0.0.1:8000' + self.image.url
    #     return ''
    
    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return 'http://127.0.0.1:8000' + self.thumbnail.url
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()

    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
    #         else:
    #             return ''
    
    # def make_thumbnail(self, image, size=(300, 200)):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)

    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)

    #     thumbnail = File(thumb_io, name=image.name)

    #     return thumbnail
