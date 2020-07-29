from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='categories_store')

    def __str__(self):
        return self.name

    def get_url(self):
        return self.icon.url

    class Meta:
        verbose_name_plural = 'Categories'


class Level(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level'


class Words(models.Model):
    name = models.CharField(max_length=100)
    translation = models.CharField(max_length=150)
    transcription = models.CharField(max_length=150)
    example = models.TextField()
    sound = models.FileField(upload_to='musics')

    def __str__(self):
        return self.name

    def get_url(self):
        return self.sound.url

    class Meta:
        verbose_name_plural = 'Words'


class Themes(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='themes_store')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    level = models.ManyToManyField(Level)
    words = models.ManyToManyField(Words)

    def __str__(self):
        return self.name

    def get_url(self):
        return self.photo.url

    class Meta:
        verbose_name_plural = 'Themes'
