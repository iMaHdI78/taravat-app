# Generated by Django 4.2.3 on 2023-08-05 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0010_rename_title_company_insurance_information_company_insurance_information_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_insurance_information',
            old_name='company_insurance_information',
            new_name='Company_insurance_information',
        ),
        migrations.RemoveField(
            model_name='tax_information',
            name='general_company_information',
        ),
    ]