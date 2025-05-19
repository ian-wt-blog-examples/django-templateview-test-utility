from django.urls import path

from .views import DemoTemplateView


urlpatterns = [
    path('', DemoTemplateView.as_view(), name='demo'),
]
