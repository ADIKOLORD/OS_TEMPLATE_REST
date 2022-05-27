import hashlib

from django.db import models

# for registration
from django.contrib.auth.models import AbstractUser


# end registration

class MyModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    description = models.TextField(verbose_name='description', blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='MyModel/%m/%d', verbose_name='Фото', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    cart = models.ManyToManyField('Cart', blank=True)
    STATUS = (
        ('NEW', 'NEW'),
        ('OLD', 'OLD'),
    )
    status = models.CharField(max_length=3, choices=STATUS, default='NEW')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'MyModel'
        verbose_name_plural = 'MyModels'


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Cart(models.Model):
    title = models.CharField(max_length=100)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.title


#######################################--REGISTER--#######################################


class MyUser(AbstractUser):
    '''
    Для добавление нового поля в регист.
    AUTH_USER_MODEL add to SETTINGS.PY
    '''
    phone_number = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['phone_number', ]

    def save(self, *args, **kwargs):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        super().save(*args, **kwargs)
