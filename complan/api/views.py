from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from .solvers import *
from .rand_string import *
import urllib.parse

# Create your views here.
class SimpleActionProcess(generics.ListAPIView):
	def get(self, request, problem):
		# pr = urllib.parse.unquote(problem)
		to_calculate = rpn(urllib.parse.unquote(problem))
		if to_calculate != "Error with brackets!":
			problem_id = rand_str()
			result = simple_action(to_calculate, problem_id)
			serializer = SolutionStepSerializer(SolutionStep.objects.filter(problem_id=problem_id), many=True)
			return Response({'response': result, 'steps': serializer.data})
		else:			
			print("Error with brackets!")
			return Response({'response': 'Error with brackets!'})
		
		
	queryset = SolutionStep.objects.all()
	serializer_class = SolutionStepSerializer
