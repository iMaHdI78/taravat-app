# Generated by Django 4.2.3 on 2023-09-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0016_alter_file_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tax_information',
            name='quarterly_information',
        ),
        migrations.RemoveField(
            model_name='tax_information',
            name='value_added_information',
        ),
        migrations.AddField(
            model_name='general_company_information',
            name='sarmaye',
            field=models.IntegerField(blank=True, null=True, verbose_name='سرمایه شرکت'),
        ),
    ]