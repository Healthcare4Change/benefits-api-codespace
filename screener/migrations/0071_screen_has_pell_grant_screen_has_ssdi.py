# Generated by Django 4.2.6 on 2023-10-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0070_remove_programeligibilitysnapshot_legal_status_required"),
    ]

    operations = [
        migrations.AddField(
            model_name="screen",
            name="has_pell_grant",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="screen",
            name="has_ssdi",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]