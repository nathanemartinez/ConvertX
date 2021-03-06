# Generated by Django 3.1.7 on 2021-04-12 00:32

import blog.utils
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210411_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='file',
            field=models.ImageField(max_length=80, upload_to=blog.utils.rename_path, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalcategory',
            name='file',
            field=models.TextField(max_length=80, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalinfopost',
            name='file',
            field=models.TextField(max_length=80, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalinfoproduct',
            name='file',
            field=models.TextField(max_length=80, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalreviewpost',
            name='file',
            field=models.TextField(max_length=80, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicalreviewproduct',
            name='file',
            field=models.TextField(max_length=80, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicaltopmoneypost',
            name='file',
            field=models.TextField(max_length=80, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='historicaltopmoneyproduct',
            name='file',
            field=models.TextField(max_length=80, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='infopost',
            name='file',
            field=models.ImageField(max_length=80, upload_to=blog.utils.rename_path, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='infoproduct',
            name='file',
            field=models.ImageField(max_length=80, upload_to=blog.utils.rename_path, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='reviewpost',
            name='file',
            field=models.ImageField(max_length=80, upload_to=blog.utils.rename_path, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='reviewproduct',
            name='file',
            field=models.ImageField(max_length=80, upload_to=blog.utils.rename_path, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='topmoneypost',
            name='file',
            field=models.ImageField(max_length=80, upload_to=blog.utils.rename_path, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='topmoneyproduct',
            name='file',
            field=models.ImageField(max_length=80, upload_to=blog.utils.rename_path, validators=[blog.validators.file_size, blog.validators.invalid_characters, blog.validators.resize_image], verbose_name='File'),
        ),
    ]
