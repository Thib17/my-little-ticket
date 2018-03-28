# Generated by Django 2.0.3 on 2018-03-27 14:57

import django.core.validators
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20180327_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='params',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='params_json',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='source',
            name='id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]