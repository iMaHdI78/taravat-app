# Generated by Django 4.2.3 on 2023-08-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0008_rename_general_company_information_company_insurance_information_company_insurance_information_and_m'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_insurance_information',
            old_name='company_insurance_information',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tax_information',
            old_name='tax_information',
            new_name='title',
        ),
    ]
