# Generated by Django 2.2 on 2021-09-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0002_alter_favourite_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]