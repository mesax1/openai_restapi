from rest_framework import serializers
from .models import ChatGPT


class ChatGPTSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatGPT
        fields = ["model", "prompt", "temperature", "max_tokens", "top_p", "n", "presence_penalty", "frequency_penalty"]