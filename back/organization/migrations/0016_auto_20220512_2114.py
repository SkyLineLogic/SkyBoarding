# Generated by Django 3.2.13 on 2022-05-12 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0015_organization_custom_email_template"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="item_id",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("added_todo", "A new to do item has been added"),
                    ("completed_todo", "To do item has been marked as completed"),
                    ("added_resource", "A new resource item has been added"),
                    ("completed_course", "Course has been completed"),
                    ("added_badge", "A new badge item has been added"),
                    ("added_introduction", "A new introduction item has been added"),
                    ("added_preboarding", "A new preboarding item has been added"),
                    ("added_new_hire", "A new hire has been added"),
                    ("added_administrator", "A new administrator has been added"),
                    ("added_manager", "A new manager has been added"),
                    ("added_admin_task", "A new admin task has been added"),
                    ("sent_email_message", "A new email has been sent"),
                    ("sent_text_message", "A new text message has been sent"),
                    ("sent_slack_message", "A new slack message has been sent"),
                    (
                        "failed_no_phone",
                        "Couldn't sent text message: number is missing",
                    ),
                    ("ran_integration", "Integration has been triggered"),
                ],
                default="added_todo",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="custom_email_template",
            field=models.TextField(
                default="",
                help_text=(
                    "Leave blank to use the default one. See documentation if you want "
                    "to use your own."
                ),
                verbose_name="Base email template",
            ),
        ),
    ]
