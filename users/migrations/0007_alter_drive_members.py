# Generated by Django 3.2.6 on 2021-10-09 06:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_alter_drive_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='members',
            field=models.ManyToManyField(related_name='in_drives', to=settings.AUTH_USER_MODEL),
        ),
    ]
