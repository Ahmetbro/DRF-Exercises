# Generated by Django 3.2.6 on 2021-09-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]