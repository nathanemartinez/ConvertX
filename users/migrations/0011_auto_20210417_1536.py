# Generated by Django 3.1.7 on 2021-04-17 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210417_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='association',
            field=models.ManyToManyField(blank=True, to='users.Association', verbose_name='Associations'),
        ),
    ]