from django.urls import path, include
from gptapi import urls as gpt_urls


urlpatterns = [
    path('chat-free/', include(gpt_urls)),
]
