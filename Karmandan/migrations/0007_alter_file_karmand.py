# Generated by Django 4.2.5 on 2023-09-06 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Karmandan', '0006_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='karmand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='Karmandan.employee_information', verbose_name='نام'),
        ),
    ]
