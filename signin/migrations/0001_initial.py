# Generated by Django 3.0.8 on 2020-08-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=50)),
                ('userPassword', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=10)),
                ('userEmail', models.CharField(max_length=50)),
                ('userGender', models.CharField(max_length=50)),
            ],
        ),
    ]
