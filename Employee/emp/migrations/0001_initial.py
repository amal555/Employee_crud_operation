# Generated by Django 4.2.11 on 2024-04-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_no', models.CharField(max_length=15)),
                ('address_details', models.JSONField(blank=True, null=True)),
                ('work_experience', models.JSONField(blank=True, null=True)),
                ('qualifications', models.JSONField(blank=True, null=True)),
                ('projects', models.JSONField(blank=True, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
