from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from google import genai
import os
from dotenv import load_dotenv
# Create your views here.
load_dotenv()



class HomeView(View):
    def get(self , request):
        return render(request , "chatbot/home.html" )
    def post(self, request):
        question = request.POST.get("question")
        if question:
            response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": question},
        ],
        stream=False
    )
            return render(request , "chatbot/home.html" , {
                "question":question,
                "response": response.choices[0].message.content
            })
        return HttpResponseRedirect(reverse_lazy("home"))
        