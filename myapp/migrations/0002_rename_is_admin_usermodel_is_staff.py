# Generated by Django 4.2.5 on 2023-10-02 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
