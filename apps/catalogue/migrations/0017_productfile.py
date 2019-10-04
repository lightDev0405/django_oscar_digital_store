# Generated by Django 2.2.5 on 2019-10-04 21:36

import apps.catalogue.storages
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_auto_20190327_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated')),
                ('file', models.FileField(storage=apps.catalogue.storages.DigitalProductStorage(), upload_to='')),
                ('checksum', models.CharField(max_length=150)),
                ('size', models.BigIntegerField()),
                ('mimetype', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='catalogue.Product')),
            ],
        ),
    ]
