# Generated by Django 3.1.7 on 2021-04-11 07:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210410_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='key',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Key'),
        ),
    ]
