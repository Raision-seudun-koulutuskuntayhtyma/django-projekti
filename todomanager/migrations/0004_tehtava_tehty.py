# Generated by Django 3.2.7 on 2021-10-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todomanager', '0003_alter_tehtava_otsikko'),
    ]

    operations = [
        migrations.AddField(
            model_name='tehtava',
            name='tehty',
            field=models.BooleanField(default=False),
        ),
    ]
