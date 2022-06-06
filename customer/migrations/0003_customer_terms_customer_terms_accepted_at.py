# Generated by Django 4.0.3 on 2022-05-11 05:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_device_deviceauthored_device_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='terms',
            field=models.CharField(blank=0, default=django.utils.timezone.now, max_length=200, null=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='terms_accepted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]