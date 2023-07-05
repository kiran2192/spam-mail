# Generated by Django 4.1.2 on 2023-06-03 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='state_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country_tb')),
            ],
        ),
        migrations.CreateModel(
            name='register_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country_tb')),
                ('stateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.state_tb')),
            ],
        ),
    ]