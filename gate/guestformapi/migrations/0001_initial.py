# Generated by Django 5.0 on 2023-12-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('entering', models.BooleanField()),
                ('roll_id', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('purpose', models.CharField(max_length=500)),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
    ]
