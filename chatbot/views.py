from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
# Create your views here.


class HomeView(View):
    def get(self , request):
        return render(request , "chatbot/home.html" )
    def post(self, View):
        pass