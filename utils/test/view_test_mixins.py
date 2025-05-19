from django.views.generic import TemplateView


# noinspection PyUnresolvedReferences
class TemplateViewTestMixin:
    error_msg = 'The required attribute %s has not been set.'

    def test_correct_template(self):
        if not getattr(self, 'view_class'):
            raise AttributeError(self.error_msg % 'view_class')
        elif not getattr(self, 'template_name'):
            raise AttributeError(self.error_msg % 'template_name')
        elif not issubclass(getattr(self, 'view_class'), TemplateView):
            raise TypeError("Attr 'view_class' not a subclass of 'TemplateView.'")

        view = self.view_class()
        self.assertEqual(view.template_name, self.template_name)

    def test_good_status_code(self):
        if not getattr(self, 'url'):
            raise AttributeError(self.error_msg % 'url')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_good_location(self):
        if not getattr(self, 'url'):
            raise AttributeError(self.error_msg % 'url')
        elif not getattr(self, 'static_url'):
            raise AttributeError(self.error_msg % 'static_url')

        self.assertEqual(self.url, self.static_url)
