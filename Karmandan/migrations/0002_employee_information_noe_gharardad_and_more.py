# Generated by Django 4.2.3 on 2023-08-07 21:03

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Karmandan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_information',
            name='noe_gharardad',
            field=models.CharField(blank=True, choices=[('gh', 'قراردادی'), ('py', 'پیمانی'), ('da', 'دوامی'), ('sa', 'ساعتی'), ('di', 'دیگر')], max_length=15, null=True, verbose_name='نوع قرارداد'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='address',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name=' آدرس'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='bimeh_code',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name=' شماره بیمه'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='birth_date',
            field=django_jalali.db.models.jDateField(blank=True, max_length=20, null=True, verbose_name=' تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='birth_place',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' محل تولد'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='family_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='father_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' نام پدر'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='madrak_tahsili',
            field=models.CharField(blank=True, choices=[('zi', 'زیر دیپلم'), ('di', 'دیپلم'), ('li', 'لیسانس'), ('fo', 'فوق لیسانس'), ('dr', 'دکترا')], max_length=100, null=True, verbose_name=' مدرک تحصیلی'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='mahale_faliat',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' محل فعالیت'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=' تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' نام'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='national_code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name=' کد ملی'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=' کد پستی'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='semat',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' سمت'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='shenasname_code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=' شماره شناسنامه'),
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=' شماره تلفن ثابت'),
        ),
    ]