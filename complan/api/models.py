from django.db import models

# Create your models here.
class SimpleAction(models.Model):  # Модель для простых действий с числами
	problem=models.TextField()  # Пример, который необходимо вычислить
	result=models.TextField()  # Результат

class SolutionStep(models.Model):  # Описание решения по шагам
	problem_id=models.TextField(max_length=15)  # Идентификатор задачи (чтобы как-то различать их)
	n=models.IntegerField()  # Описание шага
	formula=models.TextField()  # Изображение с формулой
