# Generated by Django 4.2.5 on 2023-09-08 10:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karmandan', '0008_alter_file_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='karmand',
        ),
        migrations.AddField(
            model_name='employee_information',
            name='docs',
            field=models.ManyToManyField(blank=True, to='Karmandan.file', verbose_name='مدارک بیل بیلکانه'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='karmandan/File/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='فایل'),
        ),
    ]