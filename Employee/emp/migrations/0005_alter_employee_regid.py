# Generated by Django 4.2.11 on 2024-04-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0004_remove_employee_id_alter_employee_regid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='regid',
            field=models.CharField(editable=False, max_length=20, primary_key=True, serialize=False),
        ),
    ]