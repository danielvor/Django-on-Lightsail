# Generated by Django 4.0.3 on 2022-05-17 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
