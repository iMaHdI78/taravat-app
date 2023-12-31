# Generated by Django 4.2.3 on 2023-09-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karmandan', '0013_alter_employee_information_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='phone_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sherkat', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام شرکت/موسسه')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام')),
                ('family_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خانوادگی')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='شماره تلفن ثابت')),
                ('dakheli', models.CharField(blank=True, max_length=20, null=True, verbose_name='داخلی')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='تلفن همراه')),
                ('semat', models.CharField(blank=True, max_length=100, null=True, verbose_name='سمت')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('rabet_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام رابط')),
                ('address', models.TextField(blank=True, max_length=100, null=True, verbose_name='آدرس')),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='کد پستی')),
            ],
            options={
                'verbose_name': 'دفترچه تلفن',
                'verbose_name_plural': 'دفترچه تلفن',
            },
        ),
    ]
