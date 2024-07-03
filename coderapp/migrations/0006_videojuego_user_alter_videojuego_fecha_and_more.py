# Generated by Django 5.0.6 on 2024-07-03 18:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderapp', '0005_videojuego_fecha_alter_videojuego_imagen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuego',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='videojuego_imagenes/'),
        ),
    ]
