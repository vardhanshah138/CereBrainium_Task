from django.urls import path
from .api import *


urlpatterns = [
    path('api/create',SubjectCreateApi.as_view()),
    path('api',SubjectApi.as_view()),
    path('api/<int:pk>',SubjectUpdateApi.as_view()),
]