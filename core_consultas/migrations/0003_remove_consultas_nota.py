# Generated by Django 2.1.3 on 2018-11-04 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_consultas', '0002_auto_20181104_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultas',
            name='nota',
        ),
    ]
