# Generated by Django 3.2.16 on 2022-10-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stepwise_plugin", "0003_alter_ecommerceconfiguration_course_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ecommerceeopwhitelist",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="locale",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="marketingsites",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
    ]
