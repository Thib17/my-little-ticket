# Generated by Django 2.0.3 on 2018-03-27 14:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('link', models.URLField(blank=True, max_length=1024)),
                ('py_module', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=64)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('refreshed_on', models.DateTimeField(auto_now=True)),
                ('score', models.FloatField(default=0)),
                ('summary', models.CharField(max_length=64)),
                ('text', models.TextField(blank=True, max_length=1024, null=True)),
                ('project', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=64)),
                ('assignee', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=64)),
                ('link', models.URLField(blank=True, max_length=1024)),
                ('raw', jsonfield.fields.JSONField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Board'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Source'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='tags',
            field=models.ManyToManyField(to='tickets.Tag'),
        ),
        migrations.AddField(
            model_name='board',
            name='sources',
            field=models.ManyToManyField(blank=True, to='tickets.Source'),
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together={('external_id', 'source')},
        ),
    ]