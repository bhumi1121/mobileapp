# Generated by Django 4.2.4 on 2023-08-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_cpswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(max_length=100),
        ),
    ]
