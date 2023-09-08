# Generated by Django 4.2.5 on 2023-09-06 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0013_alter_company_insurance_information_company_insurance_information_and_more'),
        ('Karmandan', '0002_employee_information_noe_gharardad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_information',
            name='sherkat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='Sherkat.general_company_information', verbose_name='نام شرکت'),
        ),
    ]
