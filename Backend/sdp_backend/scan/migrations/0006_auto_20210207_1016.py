# Generated by Django 3.1.6 on 2021-02-07 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("scan", "0005_reports_url"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Targets",
            new_name="RequestHeaders",
        ),
        migrations.RenameModel(
            old_name="SubDomains",
            new_name="ResponseHeaders",
        ),
        migrations.DeleteModel(
            name="Users",
        ),
    ]
