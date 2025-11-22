from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from google import genai
import os
from dotenv import load_dotenv
# Create your views here.
load_dotenv()
client = genai.Client()


class HomeView(View):
    def get(self , request):
        return render(request , "chatbot/home.html" )
    def post(self, request):
        question = request.POST.get("question")
        if question:
            response = client.models.generate_content( model="gemini-2.5-flash", contents=question)
            return render(request , "chatbot/home.html" , {
                "question":question,
                "response": response.text
            })
        return HttpResponseRedirect(reverse_lazy("home"))
        