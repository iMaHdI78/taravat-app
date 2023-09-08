# Generated by Django 4.2.3 on 2023-08-07 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0012_rename_quarterly_tax_information_tax_information_quarterly_information_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_insurance_information',
            name='Company_insurance_information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_insurance_information', to='Sherkat.general_company_information', verbose_name='نام شرکت / موسسه'),
        ),
        migrations.AlterField(
            model_name='tax_information',
            name='Tax_information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tax_information', to='Sherkat.general_company_information', verbose_name='نام شرکت / موسسه'),
        ),
    ]
