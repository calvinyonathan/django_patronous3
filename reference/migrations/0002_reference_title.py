# Generated by Django 3.0.7 on 2020-06-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='title',
            field=models.CharField(default=250, max_length=250),
            preserve_default=False,
        ),
    ]
