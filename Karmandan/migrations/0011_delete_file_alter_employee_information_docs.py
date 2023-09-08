# Generated by Django 4.2.5 on 2023-09-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0015_file_alter_general_company_information_postal_code_and_more'),
        ('Karmandan', '0010_remove_employee_information_folan_file_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AlterField(
            model_name='employee_information',
            name='docs',
            field=models.ManyToManyField(blank=True, to='Sherkat.file', verbose_name='مدارک'),
        ),
    ]
