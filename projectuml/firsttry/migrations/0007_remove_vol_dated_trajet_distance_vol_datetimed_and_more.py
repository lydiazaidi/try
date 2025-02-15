# Generated by Django 5.0.1 on 2024-03-03 15:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firsttry', '0006_alter_passager_id_passager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vol',
            name='dateD',
        ),
        migrations.AddField(
            model_name='trajet',
            name='distance',
            field=models.DecimalField(decimal_places=2, default='1', max_digits=10),
        ),
        migrations.AddField(
            model_name='vol',
            name='datetimeD',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vol',
            name='img',
            field=models.ImageField(default='images/default-image.jpg', upload_to=''),
        ),
    ]
