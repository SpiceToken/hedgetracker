# Generated by Django 3.1.4 on 2021-01-05 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=60)),
                ('transaction', models.CharField(max_length=70)),
                ('output_index', models.IntegerField()),
                ('low_liquidation_price', models.IntegerField()),
                ('high_liquidation_price', models.IntegerField()),
                ('earliest_liquidation_height', models.IntegerField()),
                ('maturity_height', models.IntegerField()),
                ('low_truncated_zeroes', models.CharField(max_length=10)),
                ('high_low_delta_truncated_zeroes', models.CharField(max_length=10)),
                ('hedge_units_x_sats_per_bch_high_trunc', models.IntegerField()),
                ('payout_sats_low_trunc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spending_transaction', models.CharField(max_length=70)),
                ('settlement_type', models.CharField(max_length=20)),
                ('hedge_satoshis', models.IntegerField()),
                ('long_satoshis', models.IntegerField()),
                ('oracle_price', models.IntegerField()),
                ('funding', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.funding')),
            ],
        ),
    ]
