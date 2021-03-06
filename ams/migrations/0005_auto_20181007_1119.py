# Generated by Django 2.1.2 on 2018-10-07 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0004_maintenancecharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancecharge',
            name='job_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='maintenancecharge',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.Room'),
        ),
    ]
