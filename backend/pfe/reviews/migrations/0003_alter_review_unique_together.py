# Generated by Django 4.2.7 on 2025-03-27 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishements', '0009_rename_number_room_amount_rename_number_table_amount'),
        ('accounts', '0001_initial'),
        ('reviews', '0002_delete_reviewstandard'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('profile', 'establishement')},
        ),
    ]
