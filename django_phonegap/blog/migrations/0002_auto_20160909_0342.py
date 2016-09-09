# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posting',
            options={'ordering': ['-updated_at', '-created_at']},
        ),
        migrations.RemoveField(
            model_name='posting',
            name='post',
        ),
        migrations.AddField(
            model_name='posting',
            name='title',
            field=models.CharField(default=b'Title', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posting',
            name='url',
            field=models.URLField(default=b'http://youtube.com/', max_length=400),
            preserve_default=True,
        ),
    ]
