# Generated by Django 4.2.3 on 2023-07-29 19:51

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='general_company_information',
            options={'verbose_name': 'اطلاعات عمومی شرکت', 'verbose_name_plural': 'اطلاعات عمومی شرکت ها'},
        ),
        migrations.RemoveField(
            model_name='general_company_information',
            name='Company_Activity',
        ),
        migrations.RemoveField(
            model_name='general_company_information',
            name='Tax_field',
        ),
        migrations.RemoveField(
            model_name='general_company_information',
            name='Tax_tracking_code',
        ),
        migrations.RemoveField(
            model_name='general_company_information',
            name='Type_Activity',
        ),
        migrations.RemoveField(
            model_name='general_company_information',
            name='company_Registration_date',
        ),
        migrations.RemoveField(
            model_name='general_company_information',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='general_company_information',
            name='national_id',
            field=models.FloatField(blank=True, max_length=20, null=True, verbose_name='شناسه ملی'),
        ),
        migrations.AlterField(
            model_name='general_company_information',
            name='office_address',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='آدرس دفتر'),
        ),
        migrations.AlterField(
            model_name='general_company_information',
            name='office_factory',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='آدرس کارخانه'),
        ),
        migrations.AlterField(
            model_name='general_company_information',
            name='postal_code',
            field=models.FloatField(blank=True, max_length=20, null=True, verbose_name=' کد پستی دفتر'),
        ),
        migrations.AlterField(
            model_name='general_company_information',
            name='postal_code_factory',
            field=models.FloatField(blank=True, max_length=20, null=True, verbose_name='کد پستی کارخانه'),
        ),
        migrations.AlterField(
            model_name='general_company_information',
            name='tel',
            field=models.FloatField(blank=True, max_length=12, null=True, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='general_company_information',
            name='tel_fax',
            field=models.FloatField(blank=True, max_length=12, null=True, verbose_name='شماره فکس'),
        ),
        migrations.AlterField(
            model_name='general_company_information',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='نام شرکت / موسسه'),
        ),
        migrations.AddField(
            model_name='general_company_information',
            name='company_activity',
            field=models.CharField(blank=True, choices=[('T', 'تولیدی'), ('B', 'بازرگانی'), ('KH', 'خدماتی'), ('P', 'پیمانکاری')], max_length=2, null=True, verbose_name='فعالیت شرکت'),
        ),
        migrations.AddField(
            model_name='general_company_information',
            name='company_registration_date',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ'),
        ),
        migrations.AddField(
            model_name='general_company_information',
            name='type_activity',
            field=models.CharField(blank=True, choices=[('sa', 'سهامی عام'), ('sakh', 'سهامی خاص'), ('m', 'مسئولیت محدود'), ('n', 'نسبی'), ('t', 'تضامنی'), ('s', 'سهامی'), ('ghs', 'غیر سهامی'), ('ttm', 'تعاونی تولید و مصرف')], max_length=4, null=True, verbose_name='نوع شرکت'),
        ),
    ]
