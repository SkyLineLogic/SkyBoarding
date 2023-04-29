import factory
from factory.fuzzy import FuzzyText

from .models import Integration


class IntegrationFactory(factory.django.DjangoModelFactory):
    name = FuzzyText()
    integration = 10

    class Meta:
        model = Integration


class CustomIntegrationFactory(IntegrationFactory):
    manifest = {
        "form": [
            {
                "id": "TEAM_ID",
                "url": "https://example.com/api/1.0/organizations/{{ORG}}/teams",
                "name": "Select team to add user to",
                "type": "choice",
                "data_from": "data",
                "choice_value": "gid",
                "choice_name": "name",
            }
        ],
        "exists": {
            "url": "https://example.com/api/1.0/users/{{email}}",
            "method": "GET",
            "expected": "{{email}}",
        },
        "execute": [
            {
                "url": "https://example.com/api/1.0/workspaces/{{ORG}}/addUser",
                "data": {"data": {"user": "{{email}}"}},
                "method": "POST",
            },
            {
                "url": "https://example.com/api/1.0/teams/{{TEAM_ID}}/addUser",
                "data": {"data": {"user": "{{email}}"}},
                "method": "POST",
            },
        ],
        "post_execute_notification": [
            {
                "type": "email",
                "to": "{{ email }}",
                "subject": "Created an account for ya",
                "message": "We have just created this account for you {{ first_name}}",
            }
        ],
        "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {{TOKEN}}",
        },
        "initial_data_form": [
            {
                "id": "TOKEN",
                "name": "Please put your token here",
                "description": "You can find your token here: https://....",
            },
            {
                "id": "ORG",
                "name": "Organization id",
                "description": "You can find your organization id here: https://...",
            },
            {
                "id": "PASSWORD",
                "name": "generate",
                "description": "Will be generated",
            },
        ],
        "extra_user_info": [
            {
                "id": "PERSONAL_EMAIL",
                "name": "Personal email address",
                "description": "You can find your token here: https://....",
            },
        ],
    }
