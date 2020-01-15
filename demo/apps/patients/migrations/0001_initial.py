# Generated by Django 2.2 on 2020-01-15 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('medical_record', models.CharField(db_index=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('telephone_number', models.TextField()),
                ('insurer_DID', models.TextField()),
                ('insurered_symbol', models.TextField()),
                ('insurered_number', models.IntegerField()),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
