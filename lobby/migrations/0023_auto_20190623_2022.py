# Generated by Django 2.1.7 on 2019-06-23 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0022_queue_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='lobby.Category'),
        ),
    ]
