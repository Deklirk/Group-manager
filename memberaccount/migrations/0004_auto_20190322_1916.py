# Generated by Django 2.1.5 on 2019-03-22 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberaccount', '0003_auto_20190322_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member_share',
            old_name='published_date',
            new_name='date_approved',
        ),
    ]
