# Generated by Django 5.0 on 2023-12-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("simple_app", "0004_alter_currency_codea_alter_currency_codeb"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency",
            name="date",
            field=models.IntegerField(),
        ),
    ]