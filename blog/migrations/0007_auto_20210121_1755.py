# Generated by Django 3.1.5 on 2021-01-22 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210121_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewpost',
            name='affiliate_program',
        ),
        migrations.RemoveField(
            model_name='topmoneypost',
            name='affiliate_program',
        ),
        migrations.RemoveField(
            model_name='affiliateproduct',
            name='affiliate_program',
        ),
        migrations.AddField(
            model_name='affiliateproduct',
            name='affiliate_program',
            field=models.ManyToManyField(to='blog.AffiliateProgram', verbose_name='Affiliate Program'),
        ),
    ]
