# Generated by Django 4.1.5 on 2023-01-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
