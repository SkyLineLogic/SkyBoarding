from django.urls import path

from . import views

app_name = "integrations"
urlpatterns = [
    path("slack", views.SlackOAuthView.as_view(), name="slack"),
    path("create", views.IntegrationCreateView.as_view(), name="create"),
    path(
        "delete/<int:pk>/",
        views.IntegrationDeleteView.as_view(),
        name="delete",
    ),
    path("update/<int:pk>/", views.IntegrationUpdateView.as_view(), name="update"),
    path(
        "create/google_login/",
        views.IntegrationCreateGoogleLoginView.as_view(),
        name="create-google",
    ),
    path("oauth/<int:pk>/", views.IntegrationOauthRedirectView.as_view(), name="oauth"),
    path(
        "oauth/<int:pk>/callback/",
        views.IntegrationOauthCallbackView.as_view(),
        name="oauth-callback",
    ),
    path(
        "update_creds/<int:pk>/",
        views.IntegrationUpdateExtraArgsView.as_view(),
        name="update-creds",
    ),
]
