# Generated by Django 3.2.6 on 2021-10-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaitlistEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_name', models.EmailField(max_length=255, unique=True, verbose_name='email adress')),
                ('notes', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
