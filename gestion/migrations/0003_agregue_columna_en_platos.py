# Generated by Django 5.0.2 on 2024-02-24 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_correcion_de_columna'),
    ]

    operations = [

        migrations.AddField(
            model_name='plato',
            name='tipo',
            field=models.TextField(choices=[('entrada', 'ENTRADA'), ('plato_de_fondo', 'PLATO DE FONDO'), ('postre', 'POSTRE')], default='entrada'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='platoId',
            field=models.ForeignKey(db_column='plato_id', on_delete=django.db.models.deletion.PROTECT, related_name='ingredientes', to='gestion.plato'),
        ),
        migrations.AlterField(
            model_name='preparacion',
            name='platoId',
            field=models.ForeignKey(db_column='plato_id', on_delete=django.db.models.deletion.PROTECT, related_name='preparaciones', to='gestion.plato'),
        ),
    ]
