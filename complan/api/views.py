from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from .solvers import *
import urllib.parse

# Create your views here.
class SimpleActionProcess(generics.ListAPIView):
	def get(self, request, problem):
		# pr = urllib.parse.unquote(problem)
		to_calculate = rpn(urllib.parse.unquote(problem))
		if to_calculate != "Error with brackets!":
			return Response({'response': simple_action(to_calculate)})
		else:			
			return Response({'response': 'Error with brackets!'})
		
		
	queryset = SimpleAction.objects.all()
	serializer_class = SimpleActionSerializer
