# Generated by Django 3.1.7 on 2021-04-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210410_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='key',
            field=models.UUIDField(default='a188556ba9c74b5087a5c7a67f185f3c', verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.UUIDField(default='a188556ba9c74b5087a5c7a67f185f3c', verbose_name='Key'),
        ),
    ]
