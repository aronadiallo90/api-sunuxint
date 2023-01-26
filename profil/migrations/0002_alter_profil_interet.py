# Generated by Django 4.1.5 on 2023-01-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='interet',
            field=models.CharField(choices=[('SCIENCE', 'SCIENCES'), ('FILM', 'FILM'), ('STYLE', 'Mode de Style'), ('MUSIC', 'MUSIC'), ('SANTE', 'SANTE'), ('ECONOMIE', 'ECONOMIE'), ('SPORT', 'SPORT'), ('POLITIQUE', 'POLITIQUE'), ('DIVERTISSEMENT', 'DIVERTISSEMENT')], max_length=30, verbose_name="Centre D'interêts "),
        ),
    ]