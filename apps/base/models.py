from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Settings(models.Model):
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип",
        blank = True, null = True
    )
    image_banner1 = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "banner_image",
        verbose_name="Фотография баннера №1",
        blank = True,null = True    
    )
    title_1 = models.CharField(
        max_length=255,
        verbose_name="Заголовок для фотографии №1"
    )
    image_banner2 = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "banner_image",
        verbose_name="Фотография баннера №2",
        blank = True,null = True    
    )
    title_2 = models.CharField(
        max_length=255,
        verbose_name="Заголовок для фотографии №2"
    )
    image_banner3 = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "banner_image",
        verbose_name="Фотография баннера №3",
        blank = True,null = True    
    )
    title_3 = models.CharField(
        max_length=255,
        verbose_name="Заголовок для фотографии №3"
    )

    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта',
        blank=True, null=True
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
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
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    telegram = models.URLField(
        max_length=255,
        verbose_name='Telegram',
        blank=True, null=True
    )

    
    def __str__(self):
        return self.title_1
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта "

ICON = (
    ("ИЗУЧЕНИЕ", "ИЗУЧЕНИЕ"),
    ("РАЗРАБОТКА", "РАЗРАБОТКА"),
    ("ЗАПУСК", "ЗАПУСК")
)

class OperationProcess(models.Model):
    image = models.ImageField(
        upload_to='process',
        verbose_name='фото'
    )
    title = models.TextField(
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=300,
        verbose_name='Описание'
    )
    icon = models.CharField(
        max_length=50,
        choices=ICON,
        verbose_name = 'Выберите Иконку'
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Процесс работы'


class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "about_image",
        verbose_name="Фотография",
        blank = True,null = True    
    )
    title_2 = models.CharField(
        max_length=255,
        verbose_name="Заголовок №2"
    )
    descriptions_2 = models.TextField(
        verbose_name="Описание №2"
    )
    image_2 = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "about_image",
        verbose_name="Фотография №2",
        blank = True,null = True    
    )
    youtube = models.URLField(
        verbose_name='YouTube - ссылка на видео',
        blank=True, null=True
    )
    clients = models.IntegerField(
        verbose_name='Кол-во Довольные клиенты'
    )
    staff = models.IntegerField(
        verbose_name='Кол-во опытных сотрудников'
    )
    level = models.IntegerField(
        verbose_name='Уровень удовлетворенности'
    )
    experience = models.IntegerField(
        verbose_name='Годы опыта'
    )
    awards = models.IntegerField(
        verbose_name='Награды'
    )
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

        

class Contact(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя",
        null=True,blank=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона",
        null=True,blank=True
    )
    cause = models.CharField(
        max_length=155,
        verbose_name="Причина",
        null=True,blank=True
    )
    message = models.TextField(
        verbose_name="Сообщение",
        null=True,blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оставленный отзыв"
        verbose_name_plural = "Оставленные отзывы"

class Service_Contact(models.Model):
    choice = models.CharField(
        max_length=155,
        verbose_name="Выбор услуги",
        null=True,blank=True
    )
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя",
        null=True,blank=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона",
        null=True,blank=True
    )
    email = models.URLField(
        max_length=155,
        verbose_name="Почта",
        null=True,blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оставленная заявка на услугу"
        verbose_name_plural = "Оставленная заявка на услугу"