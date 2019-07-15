# Settings file to allow parsing API documentation of Django modules,
# and provide defaults to use in the documentation.
#
# This file is placed in a subfolder,
# so the docs root is not used by find_packages()

STATIC_URL = "/static/"
SECRET_KEY = "docs"

USE_I18N = True

INSTALLED_APPS = [
    "fluent_dashboard",
    "admin_tools",
    "admin_tools.theming",
    "admin_tools.menu",
    "admin_tools.dashboard",
    "django.contrib.admin",
    "django.contrib.contenttypes",
]

ADMIN_TOOLS_INDEX_DASHBOARD = "fluent_dashboard.dashboard.FluentIndexDashboard"
ADMIN_TOOLS_APP_INDEX_DASHBOARD = "fluent_dashboard.dashboard.FluentAppIndexDashboard"
ADMIN_TOOLS_MENU = "fluent_dashboard.menu.FluentMenu"

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # / will be redirected to /<locale>/
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (),
        "OPTIONS": {
            "loaders": (
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
                "admin_tools.template_loaders.Loader",
            )
        },
    }
]
