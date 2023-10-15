# Generated by Django 4.2.5 on 2023-10-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0023_sahamdaran_father_name_sahamdaran_noe_shakhs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sahamdaran',
            name='sex',
            field=models.CharField(choices=[('f', 'زن'), ('m', 'مرد'), ('s', 'سایر')], max_length=2, null=True, verbose_name='جنسیت'),
        ),
    ]
