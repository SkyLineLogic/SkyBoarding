# Generated by Django 3.0.1 on 2020-06-08 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sequences", "0002_auto_20200606_2014"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="externalmessage",
            name="content_json",
        ),
    ]
