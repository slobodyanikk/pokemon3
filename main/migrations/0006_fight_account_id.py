# Generated by Django 4.2.6 on 2023-12-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='fight',
            name='account_id',
            field=models.CharField(default='None', max_length=30),
        ),
    ]
