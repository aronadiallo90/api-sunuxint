# Generated by Django 4.1.5 on 2023-01-26 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='', verbose_name='image')),
                ('title', models.CharField(max_length=128, verbose_name='titre')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
