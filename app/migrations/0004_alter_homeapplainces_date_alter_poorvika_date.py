# Generated by Django 4.0.6 on 2022-08-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_homeapplainces_rename_all_price_poorvika'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeapplainces',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='poorvika',
            name='date',
            field=models.DateField(),
        ),
    ]
