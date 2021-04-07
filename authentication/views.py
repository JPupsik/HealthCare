from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'sign-in.html'
