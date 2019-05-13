# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("order", "0071_secret_token")]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="secret_token",
        )
    ]
