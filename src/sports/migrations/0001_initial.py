# Generated by Django 2.0.7 on 2019-07-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.TextField()),
                ('Sport_description', models.TextField()),
            ],
        ),
    ]