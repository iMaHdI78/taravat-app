# Generated by Django 4.2.5 on 2023-10-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sherkat', '0024_sahamdaran_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='sahamdaran',
            name='check_box',
            field=models.BooleanField(blank=True, default=1, null=True, verbose_name='دارای فعالیت'),
        ),
    ]
