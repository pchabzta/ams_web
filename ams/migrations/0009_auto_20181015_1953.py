# Generated by Django 2.1.2 on 2018-10-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0008_remove_tenantprofile_misc_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
