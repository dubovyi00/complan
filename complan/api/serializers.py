from rest_framework import serializers
from .models import *

class SimpleActionSerializer(serializers.ModelSerializer):
	class Meta:
		model = SimpleAction
		fields = ('problem', 'result')

	def create(self, validated_data):
		return SimpleAction.objects.create(**validated_data)		
	
	def update(self, instance, validated_data):
		instance.problem = validated_data.get('problem', instance.problem)
		instance.result = validated_data.get('result', instance.result)

		instance.save()
		return instance

class SolutionStepSerializer(serializers.ModelSerializer):
	class Meta:
		model = SolutionStep
		fields = ('problem_id', 'n', 'formula')

	def create(self, validated_data):
		return SimpleAction.objects.create(**validated_data)		
	
	def update(self, instance, validated_data):
		instance.problem_id = validated_data.get('problem_id', instance.problem_id)
		instance.n = validated_data.get('n', instance.n)
		instance.formula = validated_data.get('formula', instance.formula)

		instance.save()
		return instance

