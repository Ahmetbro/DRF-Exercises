# Generated by Django 2.2 on 2021-10-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20211006_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(choices=[('G', 'Not Urgent'), ('R', 'Urgent')], max_length=100),
        ),
    ]
