# Generated by Django 2.0.3 on 2018-04-09 09:04

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20180327_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='params_json',
        ),
        migrations.AlterField(
            model_name='source',
            name='params',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board', to='tickets.Board'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='tickets.Source'),
        ),
    ]
