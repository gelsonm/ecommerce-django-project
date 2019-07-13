# Generated by Django 2.2.2 on 2019-07-12 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0002_auto_20190711_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
