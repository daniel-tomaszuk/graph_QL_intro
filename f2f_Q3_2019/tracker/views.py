from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from f2f_Q3_2019.settings import AWS_URL_ENDPOINT


class MapGraphQLTemplateView(LoginRequiredMixin, TemplateView):
    """
    Servers map template for GraphQL API.
    """

    template_name = "tracker/map_graphql_template.html"
    login_url = reverse_lazy("admin:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("backend_url", AWS_URL_ENDPOINT)
        return context


class MapRESTTemplateView(LoginRequiredMixin, TemplateView):
    """
    Serves map template for REST API.
    """

    template_name = "tracker/map_rest_template.html"
    login_url = reverse_lazy("admin:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
