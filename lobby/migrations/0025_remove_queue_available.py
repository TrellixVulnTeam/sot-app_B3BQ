# Generated by Django 2.1.7 on 2019-06-25 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0024_auto_20190623_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queue',
            name='available',
        ),
    ]