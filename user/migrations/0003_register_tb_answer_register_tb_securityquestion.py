# Generated by Django 4.1.2 on 2023-06-03 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_hobby_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_tb',
            name='answer',
            field=models.CharField(default='abc', max_length=20),
        ),
        migrations.AddField(
            model_name='register_tb',
            name='securityquestion',
            field=models.CharField(default='abc', max_length=20),
        ),
    ]
