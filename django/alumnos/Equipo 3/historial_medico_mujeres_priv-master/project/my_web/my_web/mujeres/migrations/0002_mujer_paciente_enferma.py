# Generated by Django 2.2.7 on 2019-11-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mujeres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mujer',
            name='paciente_enferma',
            field=models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False),
        ),
    ]