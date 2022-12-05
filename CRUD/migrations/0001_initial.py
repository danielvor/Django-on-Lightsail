# Generated by Django 4.0.3 on 2022-03-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=40)),
                ('purchase', models.CharField(max_length=10)),
                ('sale', models.CharField(max_length=10)),
                ('qty', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('U', 'U')], max_length=1, null=True)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
