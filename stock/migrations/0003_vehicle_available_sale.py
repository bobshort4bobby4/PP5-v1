# Generated by Django 3.2 on 2022-08-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_rename_type_maker_maker'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='available_sale',
            field=models.BooleanField(default=True),
        ),
    ]