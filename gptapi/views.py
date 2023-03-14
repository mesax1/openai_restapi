from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatGPT
from .serializers import ChatGPTSerializer
import openai
import os


openai.api_key = os.environ.get("OPENAI_API_KEY")

def call_chatgpt_api(serialized_data):
    if serialized_data["model"] == "text-davinci-003":
        return openai.Completion.create(model="text-davinci-003", prompt=serialized_data['prompt'], temperature=serialized_data['temperature'], max_tokens=serialized_data['max_tokens'])
    else:
        return openai.ChatCompletion.create(model=serialized_data["model"], messages = [{"role": "user", "content": f"{serialized_data['prompt']}"}], temperature=serialized_data['temperature'], max_tokens=serialized_data['max_tokens'])
          



class ChatGPTApiView(APIView):
    
    def post(self, request, *args, **kwargs):
        '''
        Create the ChatGPT API querys with the information supplied in POST.
        Required in POST:
        model
        prompt

        Optional in POST:
        temperature -> default = 1 
        max_tokens -> default = 1000
        top_p -> default = 1
        n -> default = 1 
        presence_penalty -> default = 0
        frequency_penalty -> default = 0
        '''
        data = {
            'model': request.data.get('model'), 
            'prompt': request.data.get('prompt'),
            'temperature': request.data.get('temperature', 1),
            'max_tokens':  request.data.get('max_tokens', 1000),
            'top_p': request.data.get('top_p', 1),
            'n':  request.data.get('n', 1),
            'presence_penalty': request.data.get('presence_penalty', 0),
            'frequency_penalty':  request.data.get('frequency_penalty', 0)
        }

        serializer = ChatGPTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            try:
                openai_response = call_chatgpt_api(serializer.data)
            except openai.error.APIError as openai_error:
                return Response(f"{openai_error.error.type}: {openai_error.error.message}", status=status.HTTP_406_NOT_ACCEPTABLE)
            except openai.error.APIConnectionError as openai_error:
                return Response(f"{openai_error.error.type}: {openai_error.error.message}", status=status.HTTP_406_NOT_ACCEPTABLE)
            except openai.error.RateLimitError as openai_error:
                return Response(f"{openai_error.error.type}: {openai_error.error.message}", status=status.HTTP_406_NOT_ACCEPTABLE)
            except openai.error.Timeout as openai_error:
                return Response(f"{openai_error.error.type}: {openai_error.error.message}", status=status.HTTP_406_NOT_ACCEPTABLE)
            except openai.error.InvalidRequestError as openai_error:
                return Response(f"{openai_error.error.type}: {openai_error.error.message}", status=status.HTTP_406_NOT_ACCEPTABLE)
            except openai.error.AuthenticationError as openai_error:
                return Response(f"{openai_error.error.type}: {openai_error.error.message}", status=status.HTTP_406_NOT_ACCEPTABLE)
            except openai.error.ServiceUnavailableError as openai_error:
                return Response(f"{openai_error.error.type}: {openai_error.error.message}", status=status.HTTP_406_NOT_ACCEPTABLE)
            if openai_response:
                return Response(openai_response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)