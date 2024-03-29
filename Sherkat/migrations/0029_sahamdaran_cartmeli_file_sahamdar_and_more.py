# Generated by Django 4.2.5 on 2023-11-20 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0028_rename_company_insurance_information_company_insurance_information_name_sherkat'),
    ]

    operations = [
        migrations.AddField(
            model_name='sahamdaran',
            name='cartmeli_file_sahamdar',
            field=models.FileField(blank=True, null=True, upload_to='karmandan/melicard/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])], verbose_name='فایل کارت ملی'),
        ),
        migrations.AddField(
            model_name='sahamdaran',
            name='shenasname_file_sahamdar',
            field=models.FileField(blank=True, null=True, upload_to='karmandan/shenasname/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])], verbose_name='فایل شناسنامه'),
        ),
        migrations.AlterField(
            model_name='sahamdaran',
            name='sex',
            field=models.CharField(choices=[('f', 'زن'), ('m', 'مرد')], max_length=2, null=True, verbose_name='جنسیت'),
        ),
    ]
