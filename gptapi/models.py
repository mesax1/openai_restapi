from django.db import models


class ChatGPT(models.Model):
    model = models.CharField(max_length = 180, default='gpt-3.5-turbo-0301')
    prompt = models.TextField(blank=False, default='Respondeme cualquier cosa en frances')
    temperature = models.FloatField(default=1)
    max_tokens = models.IntegerField(default=1000)
    top_p = models.FloatField(default=1)
    n = models.IntegerField(default=1)
    presence_penalty = models.FloatField(default=0)
    frequency_penalty = models.FloatField(default=0)

    def __str__(self):
        return self.task