from django.db import models
from django_resized.forms import ResizedImageField


# Create your models here.
class Team(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    job = models.CharField(
        max_length=255,
        verbose_name="Должность"
    )
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to='teacher_img/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    descriptions = models.TextField(
        max_length=255,
        verbose_name="О участнике команды"
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True, null=True
    )
    skype = models.URLField(
        verbose_name='Skype',
        blank=True, null=True
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"