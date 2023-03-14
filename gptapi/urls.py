from django.urls import path
from .views import (ChatGPTApiView,)


urlpatterns = [
    path('', ChatGPTApiView.as_view())
]