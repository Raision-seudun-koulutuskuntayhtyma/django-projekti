# Generated by Django 3.2.7 on 2021-10-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tehtava',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otsikko', models.CharField(max_length=200)),
            ],
        ),
    ]
