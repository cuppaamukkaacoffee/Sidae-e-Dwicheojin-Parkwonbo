# Generated by Django 2.2.13 on 2021-02-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scan", "0003_auto_20210206_1011"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reports",
            old_name="url",
            new_name="sub_path",
        ),
        migrations.AddField(
            model_name="reports",
            name="target",
            field=models.TextField(default=""),
        ),
    ]