# Generated by Django 3.1.5 on 2021-02-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210221_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='file',
            field=models.ImageField(blank=True, default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalcategory',
            name='file',
            field=models.TextField(blank=True, default='blog/images/default.jpg', max_length=100, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalinfopost',
            name='file',
            field=models.TextField(blank=True, default='blog/images/default.jpg', max_length=100, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalinfoproduct',
            name='file',
            field=models.TextField(blank=True, default='blog/images/default.jpg', max_length=100, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalreviewpost',
            name='file',
            field=models.TextField(blank=True, default='blog/images/default.jpg', max_length=100, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalreviewproduct',
            name='file',
            field=models.TextField(blank=True, default='blog/images/default.jpg', max_length=100, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicaltopmoneypost',
            name='file',
            field=models.TextField(blank=True, default='blog/images/default.jpg', max_length=100, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicaltopmoneyproduct',
            name='file',
            field=models.TextField(blank=True, default='blog/images/default.jpg', max_length=100, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='infopost',
            name='file',
            field=models.ImageField(blank=True, default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='infoproduct',
            name='file',
            field=models.ImageField(blank=True, default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='reviewpost',
            name='file',
            field=models.ImageField(blank=True, default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='reviewproduct',
            name='file',
            field=models.ImageField(blank=True, default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='topmoneypost',
            name='file',
            field=models.ImageField(blank=True, default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='topmoneyproduct',
            name='file',
            field=models.ImageField(blank=True, default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File'),
        ),
    ]