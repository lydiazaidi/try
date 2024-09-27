# Generated by Django 5.0.1 on 2024-02-18 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('num_avion', models.IntegerField(primary_key=True, serialize=False)),
                ('autonomie', models.IntegerField()),
                ('moteur', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id_categorie', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('type', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('capacite', models.IntegerField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('pass_field', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id_reservation', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('heur', models.TimeField()),
                ('nbr_places', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('idville', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Avion_classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numavion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.avion')),
                ('typeclasse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Passager',
            fields=[
                ('id_passager', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('dateN', models.DateField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.categorie')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.client')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationClasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.classe')),
                ('id_reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.client')),
                ('id_reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('idtrajet', models.IntegerField(primary_key=True, serialize=False)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=15)),
                ('duree', models.DurationField()),
                ('villeA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trajets_arrival', to='firsttry.ville')),
                ('villeD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trajets_departure', to='firsttry.ville')),
            ],
        ),
        migrations.CreateModel(
            name='Vol',
            fields=[
                ('num_vol', models.IntegerField(primary_key=True, serialize=False)),
                ('dateD', models.TimeField()),
                ('trajet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.trajet')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='vol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.vol'),
        ),
        migrations.CreateModel(
            name='AvionVol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.avion')),
                ('num_vol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firsttry.vol')),
            ],
        ),
    ]
