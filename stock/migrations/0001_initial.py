# Generated by Django 3.2 on 2022-08-02 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Bmw', 'Bmw'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Toyota', 'Toyota'), ('Nissan', 'Nissan'), ('Mazda', 'Mazda'), ('Mercedes', 'Mercedes')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('stock_num', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('featured', models.BooleanField(default=True)),
                ('preowned', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('odometer', models.IntegerField()),
                ('colour', models.CharField(max_length=25)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.fueltype')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.maker')),
            ],
        ),
    ]
