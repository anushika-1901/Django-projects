# Generated by Django 4.1.7 on 2025-01-31 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0008_alter_reportcard_date_of_report_card_generation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
