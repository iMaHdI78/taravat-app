# Generated by Django 4.2.3 on 2023-08-04 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0007_tax_information_general_company_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_insurance_information',
            old_name='general_company_information',
            new_name='company_insurance_information',
        ),
        migrations.RenameField(
            model_name='tax_information',
            old_name='general_company_information',
            new_name='tax_information',
        ),
    ]
