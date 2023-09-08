# Generated by Django 4.2.3 on 2023-08-05 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0011_rename_company_insurance_information_company_insurance_information_company_insurance_information_and'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tax_information',
            old_name='quarterly_tax_information',
            new_name='quarterly_information',
        ),
        migrations.AddField(
            model_name='tax_information',
            name='Tax_information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tax_information', to='Sherkat.general_company_information', verbose_name='نام شرکت / موسسه'),
        ),
    ]
