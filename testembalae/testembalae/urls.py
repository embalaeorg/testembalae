from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("testembalae.base.urls")),
    path("api/accounts/", include("testembalae.accounts.urls")),
    path(
        "api/core/",
        include("testembalae.core.urls"),
    ),
    path("", TemplateView.as_view(template_name="base/apihome.html")),
]
