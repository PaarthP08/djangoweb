# Generated by Django 3.2.6 on 2022-01-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
