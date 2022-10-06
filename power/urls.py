from django.urls import path
from power import views as power_views

urlpatterns = [
    path("", power_views.MyTemplateView.as_view(), name="template_view"),
]
