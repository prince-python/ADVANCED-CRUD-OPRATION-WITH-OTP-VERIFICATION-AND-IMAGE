# Generated by Django 4.1.4 on 2023-02-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_data_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='img',
            field=models.URLField(),
        ),
    ]
