# Generated by Django 5.0.1 on 2024-03-08 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firsttry', '0010_alter_trajet_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passager',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firsttry.categorie'),
        ),
    ]