import factory
from factory.fuzzy import FuzzyText
from pytest_factoryboy import register

from admin.introductions.models import Introduction
from users.factories import EmployeeFactory


@register
class IntroductionFactory(factory.django.DjangoModelFactory):
    name = FuzzyText()
    intro_person = factory.SubFactory(EmployeeFactory)

    class Meta:
        model = Introduction
