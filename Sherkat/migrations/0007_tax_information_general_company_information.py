# Generated by Django 4.2.3 on 2023-08-04 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0006_company_insurance_information_general_company_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax_information',
            name='general_company_information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tax_information', to='Sherkat.general_company_information', verbose_name='نام شرکت / موسسه'),
        ),
    ]
