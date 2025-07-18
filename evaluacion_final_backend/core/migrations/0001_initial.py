# Generated by Django 5.2.4 on 2025-07-12 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('entrenador', models.CharField(max_length=100)),
                ('escudo', models.ImageField(upload_to='escudos/')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EquipoTorneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('posicion', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='fotos_jugadores/')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='core.equipo')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais'),
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('equipos', models.ManyToManyField(through='core.EquipoTorneo', to='core.equipo')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('goles_local', models.IntegerField()),
                ('goles_visitante', models.IntegerField()),
                ('equipo_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_local', to='core.equipo')),
                ('equipo_visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_visitante', to='core.equipo')),
                ('torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.torneo')),
            ],
        ),
        migrations.AddField(
            model_name='equipotorneo',
            name='torneo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.torneo'),
        ),
        migrations.AlterUniqueTogether(
            name='equipotorneo',
            unique_together={('equipo', 'torneo')},
        ),
    ]
