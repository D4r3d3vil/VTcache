# Generated by Django 4.2.17 on 2025-01-11 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('url', 'URL'), ('ip', 'IP'), ('domain', 'Domain')], max_length=10)),
                ('result', models.JSONField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]