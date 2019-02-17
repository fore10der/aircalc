# Generated by Django 2.1.7 on 2019-02-17 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='AircartCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='AircartFlightRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('count', models.PositiveIntegerField(default=0)),
                ('aircart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aircarts.Aircart')),
            ],
        ),
        migrations.AddField(
            model_name='aircart',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aircarts.AircartCompany'),
        ),
    ]
