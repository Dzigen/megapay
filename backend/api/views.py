from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class LandingAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello from LandingAPIView"})

class UserSuggestionsAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello from UserSuggestionsAPIView"})