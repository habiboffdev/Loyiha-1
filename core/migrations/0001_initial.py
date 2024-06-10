# Generated by Django 4.2.3 on 2024-06-03 16:34

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('uid', models.IntegerField(unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('rating', models.BigIntegerField(default=0)),
                ('full_name', models.TextField(blank=True, null=True)),
                ('username', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code=False, message='Username can only contain letters, numbers and underscores', regex='^[a-zA-Z0-9_]+$')])),
                ('platform', models.CharField(choices=[(0, 'telegram'), (1, 'website')], default=0, max_length=2)),
                ('step', models.IntegerField(blank=True, default=0, null=True)),
                ('temp_data', models.TextField(blank=True, null=True)),
                ('magic_word', models.CharField(blank=True, max_length=63, null=True)),
                ('welcome_message_id', models.IntegerField(blank=True, null=True)),
                ('agreement_time', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
