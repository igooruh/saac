# Generated by Django 2.1.3 on 2018-11-04 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0001_initial'),
        ('core_consultas', '0003_remove_consultas_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultas',
            name='comentario',
            field=models.ManyToManyField(to='comentario.Comentario'),
        ),
    ]