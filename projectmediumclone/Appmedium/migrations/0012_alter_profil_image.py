# Generated by Django 4.1.10 on 2023-09-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appmedium', '0011_alter_profil_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='image',
            field=models.ImageField(default='img/person.png', upload_to='ProfilImage'),
        ),
    ]
