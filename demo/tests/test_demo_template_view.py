from django.test import TestCase
from django.urls import reverse

from ..views import DemoTemplateView


class TestDemoTemnplateView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('demo')
        cls.template_name = 'demo/demo-template.html'

    def test_correct_template_used_alt(self):
        view = DemoTemplateView()
        self.assertEqual(
            view.template_name,
            self.template_name
        )

    def test_good_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_good_location(self):
        self.assertEqual(self.url, '/')
