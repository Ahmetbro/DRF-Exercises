# Generated by Django 2.2 on 2021-10-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='waitlistentry',
            options={'verbose_name_plural': 'Waitlist Entries'},
        ),
        migrations.AlterField(
            model_name='waitlistentry',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]