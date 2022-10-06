from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from power.models import FiveYearPlan


class MyTemplateView(TemplateView):
    template_name = "index.html"


class FiveYearPlanListView(LoginRequiredMixin, ListView):
    model = FiveYearPlan
    template_name = "five_year_plan_list_view.html"
