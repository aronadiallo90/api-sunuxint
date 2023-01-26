from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profil(models.Model):

    
    SCIENCE = 'SCIENCE'
    FILM = 'FILM'
    MUSIC = 'MUSIC'
    STYLE= 'STYLE'
    SANTE = 'SANTE'
    ECONOMIE ='ECONOMIE'
    SPORT = 'SPORT'
    POLITIQUE = 'POLITIQUE'
    DIVERTISSEMENT = 'DIVERTISSEMENT'

    CENTRE_INTERET_CHOICES = (
        (SCIENCE, 'SCIENCES'),
        (FILM, 'FILM'),
        ( STYLE,'Mode de Style'),
        (MUSIC , 'MUSIC'),
        (SANTE , 'SANTE'),
        (ECONOMIE ,'ECONOMIE'),
        (SPORT , 'SPORT'),
        (POLITIQUE , 'POLITIQUE'),
        (DIVERTISSEMENT , 'DIVERTISSEMENT'),
     
    )
    # interet = models.CharField (choices =CENTRE_INTERET_CHOICES)
    profile_photo = models.ImageField(verbose_name='photo de profil')
    username  = models.CharField(max_length=128, verbose_name='nom')
    interet = models.CharField(max_length=30, choices=CENTRE_INTERET_CHOICES, verbose_name='Centre D\'interêts ')
    biographie = models.TextField(max_length=1024, verbose_name='Biographie')