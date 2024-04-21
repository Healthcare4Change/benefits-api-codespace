# Generated by Django 4.2.6 on 2024-04-21 17:17

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import translations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Translation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("no_auto", models.BooleanField(default=False)),
                ("label", models.CharField(max_length=128, unique=True)),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
            managers=[
                ("objects", translations.models.TranslationManager()),
            ],
        ),
        migrations.CreateModel(
            name="TranslationTranslation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                ("text", models.TextField(blank=True, null=True)),
                ("edited", models.BooleanField(default=False)),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="translations.translation",
                    ),
                ),
            ],
            options={
                "verbose_name": "translation Translation",
                "db_table": "translations_translation_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
