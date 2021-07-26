from django.db import models

# Create your models here.
class SimpleAction(models.Model):  # Модель для простых действий с числами
	problem=models.TextField()  # Пример, который необходимо вычислить
	result=models.TextField()  # Результат

class SolutionStep(models.Model):  # Описание решения по шагам
	desription=models.TextField()  # Описание шага
	formula_url=models.TextField()  # Изображение с формулой
