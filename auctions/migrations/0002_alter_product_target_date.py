# Generated by Django 4.1.7 on 2023-03-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='target_date',
            field=models.DateTimeField(null=True),
        ),
    ]