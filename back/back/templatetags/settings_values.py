# Source: https://stackoverflow.com/a/7716141
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def aws_enabled():
    return settings.AWS_STORAGE_BUCKET_NAME != ""


@register.simple_tag
def text_enabled():
    return settings.TWILIO_FROM_NUMBER != ""
