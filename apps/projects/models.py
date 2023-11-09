from django.db import models
from django_resized.forms import ResizedImageField


# Create your models here.
class Projects(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название проекта'
    )
    descriptions = models.TextField(
        verbose_name='Описание проекта'
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "service_image/",
        verbose_name="Фотография проекта",
        blank = True,null = True    
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Наши проекты"
        verbose_name_plural = "Наши проекты"