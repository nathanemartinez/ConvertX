# Generated by Django 3.1.5 on 2021-02-16 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210215_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normallink',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='normallink',
            name='updater',
        ),
        migrations.DeleteModel(
            name='HistoricalNormalLink',
        ),
        migrations.DeleteModel(
            name='NormalLink',
        ),
    ]