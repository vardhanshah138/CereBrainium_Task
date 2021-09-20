from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import *


class SubjectCreateApi(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer