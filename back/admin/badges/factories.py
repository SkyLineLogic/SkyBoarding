import factory
from factory.fuzzy import FuzzyText
from pytest_factoryboy import register

from admin.badges.models import Badge


@register
class BadgeFactory(factory.django.DjangoModelFactory):
    name = FuzzyText()
    content = {
        "time": 0,
        "blocks": [
            {"data": {"text": "Well done!"}, "type": "paragraph"},
            {"data": {"text": "Well done!"}, "type": "paragraph"},
        ],
    }

    class Meta:
        model = Badge
