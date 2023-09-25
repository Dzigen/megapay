from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import test

# Create your views here.

class LandingAPIView(APIView):
    def get(self, request):
        values = test.objects.all()[0].text_d
        return Response({"message": "Hello from LandingAPIView", 'data': values})

class UserSuggestionsAPIView(APIView):
    def get(self, request):
        values = test.objects.all()[0].text_d
        return Response({"message": "Hello from UserSuggestionsAPIView", 'data': values})