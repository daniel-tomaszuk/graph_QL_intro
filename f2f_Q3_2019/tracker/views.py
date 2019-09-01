from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class MapGraphQLTemplateView(LoginRequiredMixin, TemplateView):
    """
    Servers map template for GraphQL API.
    """
    template_name = 'tracker/map_graphql_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MapRESTTemplateView(LoginRequiredMixin, TemplateView):
    """
    Serves map template for REST API.
    """
    template_name = 'tracker/map_rest_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
