# Generated by Django 2.1.5 on 2019-02-09 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter', models.CharField(max_length=16)),
                ('file', models.FileField(upload_to='reports/')),
                ('generate_date', models.DateField(auto_now_add=True)),
                ('report_date_start', models.DateField()),
                ('report_date_end', models.DateField()),
            ],
        ),
    ]
