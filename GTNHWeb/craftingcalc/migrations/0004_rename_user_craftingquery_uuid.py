# Generated by Django 4.1 on 2023-07-29 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('craftingcalc', '0003_authenticateduser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='craftingquery',
            old_name='user',
            new_name='uuid',
        ),
    ]