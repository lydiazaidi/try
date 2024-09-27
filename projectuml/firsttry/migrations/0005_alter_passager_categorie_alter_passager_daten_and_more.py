# Generated by Django 5.0.1 on 2024-02-20 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firsttry', '0004_alter_passager_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passager',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firsttry.categorie'),
        ),
        migrations.AlterField(
            model_name='passager',
            name='dateN',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='passager',
            name='nom',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='passager',
            name='prenom',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
