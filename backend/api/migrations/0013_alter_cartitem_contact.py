# Generated by Django 4.0 on 2024-09-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_cartitem_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
