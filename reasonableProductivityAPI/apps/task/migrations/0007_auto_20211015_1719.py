# Generated by Django 2.2 on 2021-10-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20211015_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(choices=[('G', 'Not Urgent'), ('R', 'Urgent')], max_length=100),
        ),
    ]
