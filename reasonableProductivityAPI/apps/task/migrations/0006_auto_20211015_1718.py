# Generated by Django 2.2 on 2021-10-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20211007_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(choices=[('R', 'Urgent'), ('G', 'Not Urgent')], max_length=100),
        ),
    ]
