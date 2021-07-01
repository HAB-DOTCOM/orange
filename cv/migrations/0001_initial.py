# Generated by Django 3.0.8 on 2021-07-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=250)),
                ('Lastname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('dateofbirth', models.DateTimeField(auto_now_add=True)),
                ('phonenumber', models.TextField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='experts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=250)),
                ('Lastname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('levelofstudy', models.CharField(max_length=250)),
            ],
        ),
    ]
