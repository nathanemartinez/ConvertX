# Generated by Django 3.1.5 on 2021-02-13 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20210213_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalInfoLink',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Updated')),
                ('follow', models.CharField(choices=[('NF', 'No Follow'), ('DF', 'Do Follow')], max_length=10, verbose_name='Follow')),
                ('link', models.URLField(max_length=500, verbose_name='Link')),
                ('anchor_text', models.CharField(max_length=30, verbose_name='Anchor Text')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('creator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Info Link',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInfoProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Updated')),
                ('alt_tag', models.CharField(max_length=50, null=True, verbose_name='Alt Tag')),
                ('caption', models.TextField(max_length=100, null=True, verbose_name='Caption')),
                ('file', models.TextField(default='blog/images/default.jpg', max_length=100, verbose_name='File')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', tinymce.models.HTMLField()),
                ('sku_asin', models.CharField(max_length=50, verbose_name='Sku or Asin')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('currency', models.CharField(default='USD', max_length=10, verbose_name='Currency')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Manufacturer')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('creator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'historical Info Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReviewLink',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Updated')),
                ('follow', models.CharField(choices=[('NF', 'No Follow'), ('DF', 'Do Follow')], max_length=10, verbose_name='Follow')),
                ('link', models.URLField(max_length=500, verbose_name='Link')),
                ('anchor_text', models.CharField(max_length=30, verbose_name='Anchor Text')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('creator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Review Link',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReviewProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Updated')),
                ('alt_tag', models.CharField(max_length=50, null=True, verbose_name='Alt Tag')),
                ('caption', models.TextField(max_length=100, null=True, verbose_name='Caption')),
                ('file', models.TextField(default='blog/images/default.jpg', max_length=100, verbose_name='File')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', tinymce.models.HTMLField()),
                ('sku_asin', models.CharField(max_length=50, verbose_name='Sku or Asin')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('currency', models.CharField(default='USD', max_length=10, verbose_name='Currency')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Manufacturer')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('creator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'historical Review Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTopMoneyLink',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Updated')),
                ('follow', models.CharField(choices=[('NF', 'No Follow'), ('DF', 'Do Follow')], max_length=10, verbose_name='Follow')),
                ('link', models.URLField(max_length=500, verbose_name='Link')),
                ('anchor_text', models.CharField(max_length=30, verbose_name='Anchor Text')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('creator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Top Money Link',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTopMoneyProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Date Updated')),
                ('alt_tag', models.CharField(max_length=50, null=True, verbose_name='Alt Tag')),
                ('caption', models.TextField(max_length=100, null=True, verbose_name='Caption')),
                ('file', models.TextField(default='blog/images/default.jpg', max_length=100, verbose_name='File')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', tinymce.models.HTMLField()),
                ('sku_asin', models.CharField(max_length=50, verbose_name='Sku or Asin')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('currency', models.CharField(default='USD', max_length=10, verbose_name='Currency')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Manufacturer')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('creator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'historical Top Money Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='InfoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('follow', models.CharField(choices=[('NF', 'No Follow'), ('DF', 'Do Follow')], max_length=10, verbose_name='Follow')),
                ('link', models.URLField(max_length=500, verbose_name='Link')),
                ('anchor_text', models.CharField(max_length=30, verbose_name='Anchor Text')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infolink_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'verbose_name': 'Info Link',
                'verbose_name_plural': 'Info Links',
            },
        ),
        migrations.CreateModel(
            name='InfoProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('alt_tag', models.CharField(max_length=50, null=True, verbose_name='Alt Tag')),
                ('caption', models.TextField(max_length=100, null=True, verbose_name='Caption')),
                ('file', models.ImageField(default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', tinymce.models.HTMLField()),
                ('sku_asin', models.CharField(max_length=50, verbose_name='Sku or Asin')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('currency', models.CharField(default='USD', max_length=10, verbose_name='Currency')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Manufacturer')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('affiliate_program', models.ManyToManyField(to='blog.AffiliateProgram', verbose_name='Affiliate Program')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infoproduct_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infoproduct_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'Info Product',
                'verbose_name_plural': 'Info Products',
            },
        ),
        migrations.CreateModel(
            name='ReviewLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('follow', models.CharField(choices=[('NF', 'No Follow'), ('DF', 'Do Follow')], max_length=10, verbose_name='Follow')),
                ('link', models.URLField(max_length=500, verbose_name='Link')),
                ('anchor_text', models.CharField(max_length=30, verbose_name='Anchor Text')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewlink_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'verbose_name': 'Review Link',
                'verbose_name_plural': 'Review Links',
            },
        ),
        migrations.CreateModel(
            name='ReviewProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('alt_tag', models.CharField(max_length=50, null=True, verbose_name='Alt Tag')),
                ('caption', models.TextField(max_length=100, null=True, verbose_name='Caption')),
                ('file', models.ImageField(default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', tinymce.models.HTMLField()),
                ('sku_asin', models.CharField(max_length=50, verbose_name='Sku or Asin')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('currency', models.CharField(default='USD', max_length=10, verbose_name='Currency')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Manufacturer')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('affiliate_program', models.ManyToManyField(to='blog.AffiliateProgram', verbose_name='Affiliate Program')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewproduct_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewproduct_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'Review Product',
                'verbose_name_plural': 'Review Products',
            },
        ),
        migrations.CreateModel(
            name='TopMoneyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('follow', models.CharField(choices=[('NF', 'No Follow'), ('DF', 'Do Follow')], max_length=10, verbose_name='Follow')),
                ('link', models.URLField(max_length=500, verbose_name='Link')),
                ('anchor_text', models.CharField(max_length=30, verbose_name='Anchor Text')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topmoneylink_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'verbose_name': 'Top Money Link',
                'verbose_name_plural': 'Top Money Links',
            },
        ),
        migrations.CreateModel(
            name='TopMoneyProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('alt_tag', models.CharField(max_length=50, null=True, verbose_name='Alt Tag')),
                ('caption', models.TextField(max_length=100, null=True, verbose_name='Caption')),
                ('file', models.ImageField(default='blog/images/default.jpg', upload_to='blog/images/', verbose_name='File')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', tinymce.models.HTMLField()),
                ('sku_asin', models.CharField(max_length=50, verbose_name='Sku or Asin')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('currency', models.CharField(default='USD', max_length=10, verbose_name='Currency')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Manufacturer')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('affiliate_program', models.ManyToManyField(to='blog.AffiliateProgram', verbose_name='Affiliate Program')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topmoneyproduct_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topmoneyproduct_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'Top Money Product',
                'verbose_name_plural': 'Top Money Products',
            },
        ),
        migrations.RemoveField(
            model_name='affiliateproduct',
            name='affiliate_program',
        ),
        migrations.RemoveField(
            model_name='affiliateproduct',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='affiliateproduct',
            name='updater',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliatelink',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliatelink',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliatelink',
            name='product',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliatelink',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliatelink',
            name='updater',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliateproduct',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliateproduct',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliateproduct',
            name='updater',
        ),
        migrations.DeleteModel(
            name='AffiliateLink',
        ),
        migrations.DeleteModel(
            name='AffiliateProduct',
        ),
        migrations.DeleteModel(
            name='HistoricalAffiliateLink',
        ),
        migrations.DeleteModel(
            name='HistoricalAffiliateProduct',
        ),
        migrations.AddField(
            model_name='topmoneylink',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.topmoneyproduct', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='topmoneylink',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.affiliatetag', verbose_name='Affiliate Tag'),
        ),
        migrations.AddField(
            model_name='topmoneylink',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topmoneylink_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='reviewlink',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.reviewproduct', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='reviewlink',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.affiliatetag', verbose_name='Affiliate Tag'),
        ),
        migrations.AddField(
            model_name='reviewlink',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewlink_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='infolink',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.infoproduct', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='infolink',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.affiliatetag', verbose_name='Affiliate Tag'),
        ),
        migrations.AddField(
            model_name='infolink',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infolink_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicaltopmoneylink',
            name='product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.topmoneyproduct', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='historicaltopmoneylink',
            name='tag',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.affiliatetag', verbose_name='Affiliate Tag'),
        ),
        migrations.AddField(
            model_name='historicaltopmoneylink',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalreviewlink',
            name='product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.reviewproduct', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='historicalreviewlink',
            name='tag',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.affiliatetag', verbose_name='Affiliate Tag'),
        ),
        migrations.AddField(
            model_name='historicalreviewlink',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalinfolink',
            name='product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.infoproduct', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='historicalinfolink',
            name='tag',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='blog.affiliatetag', verbose_name='Affiliate Tag'),
        ),
        migrations.AddField(
            model_name='historicalinfolink',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
    ]
