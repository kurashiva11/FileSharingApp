# Generated by Django 3.0.5 on 2020-04-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadFiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='isprivate',
            field=models.BooleanField(default=False),
        ),
    ]
