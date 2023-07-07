# Generated by Django 4.2.3 on 2023-07-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerGoatMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_id', models.IntegerField()),
                ('goat_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BuyTran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
                ('amount_due', models.FloatField()),
                ('due_time', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
