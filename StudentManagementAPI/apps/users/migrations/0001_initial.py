# Generated by Django 3.2.6 on 2021-10-04 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_student', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('preferred_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profile-images')),
                ('discord_name', models.CharField(max_length=100)),
                ('github_name', models.CharField(max_length=100)),
                ('codepen_username', models.CharField(max_length=100)),
                ('fcc_profile_url', models.CharField(max_length=100)),
                ('current_level', models.IntegerField(choices=[(1, 'level one'), (2, 'level two')], default=1)),
                ('phone', models.CharField(max_length=50)),
                ('timezone', models.CharField(max_length=50)),
            ],
        ),
    ]
