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
		fields = ('desription', 'formula_url')

	def create(self, validated_data):
		return SimpleAction.objects.create(**validated_data)		
	
	def update(self, instance, validated_data):
		instance.desription = validated_data.get('desription', instance.desription)
		instance.formula_url = validated_data.get('formula_url', instance.formula_url)

		instance.save()
		return instance

