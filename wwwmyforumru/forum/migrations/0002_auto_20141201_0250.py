# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='topic_id',
            new_name='topic',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='section_id',
            new_name='section',
        ),
    ]
