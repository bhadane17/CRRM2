# Generated by Django 4.1 on 2022-09-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screens", "0003_transaction_behavior"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction_behavior",
            name="Frquency_Three",
            field=models.IntegerField(default="3"),
        ),
        migrations.AlterField(
            model_name="transaction_behavior",
            name="Frquency_Two",
            field=models.IntegerField(default="2"),
        ),
        migrations.AlterField(
            model_name="transaction_behavior",
            name="Frquency_one",
            field=models.IntegerField(default="1"),
        ),
    ]
