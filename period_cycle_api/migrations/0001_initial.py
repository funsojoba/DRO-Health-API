# Generated by Django 3.2.5 on 2021-07-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodCylceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('cycle_average', models.IntegerField()),
                ('period_average', models.IntegerField()),
                ('total_created_cycle', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]