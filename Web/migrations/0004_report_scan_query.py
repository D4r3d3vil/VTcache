# Generated by Django 4.2.18 on 2025-01-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_alter_report_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='scan_query',
            field=models.TextField(default=''),
        ),
    ]
