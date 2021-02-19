# Generated by Django 3.1.5 on 2021-02-19 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20210216_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infopost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='reviewpost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='topmoneypost',
            name='category',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Category')),
                ('updater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalSubCategory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Updated')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('creator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.category', verbose_name='Category')),
                ('updater', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'historical Sub Category',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='historicalinfopost',
            name='subcategory',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.subcategory', verbose_name='Sub Category'),
        ),
        migrations.AddField(
            model_name='historicalreviewpost',
            name='subcategory',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.subcategory', verbose_name='Sub Category'),
        ),
        migrations.AddField(
            model_name='historicaltopmoneypost',
            name='subcategory',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.subcategory', verbose_name='Sub Category'),
        ),
        migrations.AddField(
            model_name='infopost',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.subcategory', verbose_name='Sub Category'),
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.subcategory', verbose_name='Sub Category'),
        ),
        migrations.AddField(
            model_name='topmoneypost',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.subcategory', verbose_name='Sub Category'),
        ),
    ]
