# Generated by Django 4.2.4 on 2024-02-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ScrapeData",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("ip", models.CharField(blank=True, max_length=124, null=True)),
                ("protocol", models.CharField(blank=True, max_length=124, null=True)),
                ("country", models.CharField(blank=True, max_length=124, null=True)),
                ("uptime", models.CharField(blank=True, max_length=124, null=True)),
                ("port", models.IntegerField()),
            ],
        ),
    ]
