# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("order", "0070_drop_update_event_and_rename_events")]

    operations = [
        migrations.AddField(
            model_name="order",
            name="secret_token",
            field=models.CharField(default="", max_length=32, db_index=True),
        )
    ]
