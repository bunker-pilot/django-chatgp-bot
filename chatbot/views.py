from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from google import genai
import os
from dotenv import load_dotenv
# Create your views here.
load_dotenv()
client = genai.Client(api_key="sk-de6ff67d2a0e42e0b136f832a09d33b8")


class HomeView(View):
    def get(self , request):
        return render(request , "chatbot/home.html"  , {"chat" : request.session.get("chat" , [])})
    def post(self, request):
        question = request.POST.get("question")
        if question:
            chat = request.session.get("chat",[])
            response = client.models.generate_content( model="gemini-2.5-flash", contents=question)
            chat.append({"question" : question , "response": response.text})
            request.session["chat"] = chat
            request.session.modified = True
            return render(request , "chatbot/home.html" , {
                "question":question,
                "response": response.text
            })
        return HttpResponseRedirect(reverse_lazy("home"))
        