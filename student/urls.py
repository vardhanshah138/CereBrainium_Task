from django.urls import path
from .api import *


urlpatterns = [
    path('api/create',SubjectCreateApi.as_view()),
]