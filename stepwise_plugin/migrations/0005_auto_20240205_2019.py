# Generated by Django 3.2.21 on 2024-02-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepwise_plugin', '0004_auto_20221020_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecommerceeopwhitelist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='locale',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='marketingsites',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
