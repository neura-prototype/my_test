# Generated by Django 4.0.3 on 2022-04-18 23:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsNotificationFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_us_redirect_url', models.URLField(blank=True, help_text='The URL to be visited when a notification is clicked.', max_length=500, null=True)),
                ('contact_us_verb', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_us_timestamp', models.DateTimeField(auto_now_add=True)),
                ('contact_us_read', models.BooleanField(default=False)),
                ('contact_us_from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_us_from_user', to=settings.AUTH_USER_MODEL)),
                ('contact_us_target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsFile',
            fields=[
                ('auto_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('contact_us_message', models.CharField(blank=True, max_length=500, null=True)),
                ('read_unread', models.CharField(blank=True, default=False, max_length=10, null=True)),
                ('read_time', models.DateTimeField(blank=True, default=datetime.datetime.today, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]