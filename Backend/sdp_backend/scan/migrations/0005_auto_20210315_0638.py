# Generated by Django 3.1.6 on 2021-03-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0004_responseheaders_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseheaders',
            name='body',
            field=models.BinaryField(blank=True, default=b''),
        ),
    ]
