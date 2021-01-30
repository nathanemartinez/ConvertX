# Generated by Django 3.1.5 on 2021-01-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='category',
        ),
        migrations.AddField(
            model_name='infopost',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='topmoneypost',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Tag'),
        ),
    ]