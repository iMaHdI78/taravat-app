# Generated by Django 4.2.3 on 2023-10-12 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0027_alter_company_insurance_information_company_insurance_information_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_insurance_information',
            old_name='Company_insurance_information',
            new_name='name_sherkat',
        ),
    ]
