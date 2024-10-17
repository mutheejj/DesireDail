# Generated by Django 5.0.4 on 2024-10-17 08:17

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_chatroom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, primary_key=True, serialize=False, unique=True),
        ),
    ]
