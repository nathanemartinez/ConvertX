# Generated by Django 3.1.5 on 2021-01-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20210123_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affiliatelink',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='affiliatelink',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='affiliateproduct',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='affiliateproduct',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='affiliateprogram',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='affiliateprogram',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliatelink',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliatelink',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliateproduct',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliateproduct',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliateprogram',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalaffiliateprogram',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalcategory',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalcategory',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalinfopost',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalinfopost',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalinfopostestimates',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalinfopostestimates',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalnormallink',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalnormallink',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalreviewpost',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalreviewpost',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicalreviewpostestimates',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalreviewpostestimates',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicaltag',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicaltag',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicaltopmoneypost',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicaltopmoneypost',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='historicaltopmoneypostestimates',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicaltopmoneypostestimates',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='infopost',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='infopost',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='infopostestimates',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='infopostestimates',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='normallink',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='normallink',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='reviewpost',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='reviewpost',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='reviewpostestimates',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='reviewpostestimates',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='topmoneypost',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='topmoneypost',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='topmoneypostestimates',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='topmoneypostestimates',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='affiliatelink',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affiliatelink_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='affiliatelink',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affiliatelink_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='affiliateproduct',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affiliateproduct_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='affiliateproduct',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affiliateproduct_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='affiliateprogram',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affiliateprogram_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='affiliateprogram',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affiliateprogram_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='category',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='category',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalaffiliatelink',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalaffiliatelink',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalaffiliateproduct',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalaffiliateproduct',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalaffiliateprogram',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalaffiliateprogram',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalcategory',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalcategory',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalinfopost',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalinfopost',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalinfopostestimates',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalinfopostestimates',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalnormallink',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalnormallink',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalreviewpost',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalreviewpost',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicalreviewpostestimates',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicalreviewpostestimates',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicaltag',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicaltag',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicaltopmoneypost',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicaltopmoneypost',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='historicaltopmoneypostestimates',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicaltopmoneypostestimates',
            name='updater',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='infopost',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infopost_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='infopost',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infopost_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='infopostestimates',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infopostestimates_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='infopostestimates',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infopostestimates_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='normallink',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='normallink_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='normallink',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='normallink_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewpost_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewpost_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='reviewpostestimates',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewpostestimates_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='reviewpostestimates',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewpostestimates_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='tag',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='topmoneypost',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topmoneypost_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='topmoneypost',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topmoneypost_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
        migrations.AddField(
            model_name='topmoneypostestimates',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topmoneypostestimates_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='topmoneypostestimates',
            name='updater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topmoneypostestimates_updater', to=settings.AUTH_USER_MODEL, verbose_name='Updater'),
        ),
    ]