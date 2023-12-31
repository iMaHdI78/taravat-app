# Generated by Django 4.2.5 on 2023-10-01 11:46

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0020_rename_tel_sahamdar_sahamdaran_tel_sahamdaran'),
    ]

    operations = [
        migrations.AddField(
            model_name='sahamdaran',
            name='noe_masoliat',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='نوع مسئولیت'),
        ),
        migrations.AddField(
            model_name='sahamdaran',
            name='semat_sahamdaran',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='سمت'),
        ),
        migrations.AddField(
            model_name='sahamdaran',
            name='tarikh_ozviat',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ عضویت'),
        ),
        migrations.AddField(
            model_name='sahamdaran',
            name='tarikh_payan',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='پایان کار'),
        ),
    ]
