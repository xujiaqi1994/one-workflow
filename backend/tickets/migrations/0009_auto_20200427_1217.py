# Generated by Django 3.0.2 on 2020-04-27 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20200427_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketcustomfield',
            old_name='field',
            new_name='customfield',
        ),
    ]
