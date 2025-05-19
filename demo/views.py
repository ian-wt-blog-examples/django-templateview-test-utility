from django.views.generic import TemplateView


class DemoTemplateView(TemplateView):
    template_name = 'demo/demo-template.html'
