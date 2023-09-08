# Generated by Django 4.2.3 on 2023-07-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General_company_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('tel', models.CharField(max_length=100)),
                ('tel_fax', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=100)),
                ('company_Registration_date', models.CharField(max_length=100)),
                ('postal_code_factory', models.CharField(max_length=100)),
                ('Tax_tracking_code', models.CharField(max_length=100)),
                ('Type_Activity', models.CharField(choices=[('sa', 'سهامی عام'), ('sakh', 'سهامی خاص'), ('m', 'مسئولیت محدود'), ('n', 'نسبی'), ('t', 'تضامنی'), ('s', 'سهامی'), ('ghs', 'غیر سهامی'), ('ttm', 'تعاونی تولید و مصرف')], max_length=4)),
                ('Company_Activity', models.CharField(choices=[('T', 'تولیدی'), ('B', 'بازرگانی'), ('KH', 'خدماتی'), ('P', 'پیمانکاری')], max_length=2)),
                ('office_address', models.TextField(max_length=100)),
                ('office_factory', models.TextField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='images')),
                ('Tax_field', models.CharField(max_length=100)),
            ],
        ),
    ]
