# Generated by Django 5.0 on 2023-12-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_rename_expense_name_expense_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]