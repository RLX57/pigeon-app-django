# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_text', models.CharField(max_length=140)),
                ('tweet_user', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
