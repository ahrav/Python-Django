# Generated by Django 2.2 on 2019-04-30 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
