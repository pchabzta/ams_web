# Generated by Django 2.1.2 on 2018-10-07 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0005_auto_20181007_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancecharge',
            name='job_cost',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tenantprofile',
            name='elec_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='tenantprofile',
            name='misc_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='tenantprofile',
            name='water_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
