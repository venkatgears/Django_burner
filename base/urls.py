from django.urls import path
from .views import *

urlpatterns = [
path("", Home , name="Home"), 
path("room/<slug:pk>/", Rend , name="room")
]

