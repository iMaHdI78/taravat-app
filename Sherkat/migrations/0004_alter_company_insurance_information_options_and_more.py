# Generated by Django 4.2.3 on 2023-08-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0003_company_insurance_information_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company_insurance_information',
            options={'verbose_name': 'اطلاعات بیمه ای شرکت', 'verbose_name_plural': 'اطلاعات بیمه ای شرکت ها'},
        ),
        migrations.RenameField(
            model_name='company_insurance_information',
            old_name='Name_office_insurance_branch',
            new_name='name_factory_insurance_branch',
        ),
        migrations.AddField(
            model_name='company_insurance_information',
            name='name_office_insurance_branch',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام شعبه ی بیمه دفتر'),
        ),
    ]