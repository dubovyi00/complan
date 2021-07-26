from django.urls import path
from . import views

urlpatterns = [
	path('simple_action/<str:problem>', views.SimpleActionProcess.as_view() ),
]
