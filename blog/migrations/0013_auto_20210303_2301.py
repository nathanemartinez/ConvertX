# Generated by Django 3.1.5 on 2021-03-04 07:01

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210303_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltopmoneypost',
            name='outro',
            field=tinymce.models.HTMLField(null=True, verbose_name='Outro'),
        ),
        migrations.AlterField(
            model_name='topmoneypost',
            name='outro',
            field=tinymce.models.HTMLField(null=True, verbose_name='Outro'),
        ),
    ]
