# Generated by Django 4.1.10 on 2023-08-28 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Appmedium', '0004_alter_postcreate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcreate',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
