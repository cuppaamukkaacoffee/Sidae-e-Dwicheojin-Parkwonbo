# Generated by Django 3.1.6 on 2021-03-20 04:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0006_auto_20210320_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whoiss',
            name='address',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='city',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='country',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='creation_date',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='dnssec',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='domain_name',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='expiration_date',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='name',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='name_servers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='org',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='referral_url',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='registrar',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='state',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='status',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='updated_date',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='whois_server',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='whoiss',
            name='zipcode',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
    ]
