# Generated by Django 4.0.5 on 2022-12-08 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0018_alter_navigatortranslation_cell'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navigatortranslation',
            old_name='cell',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='navigatortranslation',
            name='program',
            field=models.ManyToManyField(related_name='navigator', to='programs.program'),
        ),
    ]