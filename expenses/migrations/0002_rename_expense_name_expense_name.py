# Generated by Django 5.0 on 2023-12-09 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='expense_name',
            new_name='name',
        ),
    ]
