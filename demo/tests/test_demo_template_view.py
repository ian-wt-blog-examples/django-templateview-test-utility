from django.test import TestCase
from django.urls import reverse

from utils.test.view_test_mixins_concise import TemplateViewTestMixin
from ..views import DemoTemplateView


class TestDemoTemnplateView(TemplateViewTestMixin, TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.view_class = DemoTemplateView
        cls.template_name = 'demo/demo-template.html'
        cls.url = reverse('demo')
        cls.static_url = '/'
