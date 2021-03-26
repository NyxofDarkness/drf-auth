from django.shortcuts import render
from opinions.permission import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import OpinionSerializer
from .models import Opinions

class OpinionList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Opinions.objects.all()
    serializer_class = OpinionSerializer

class OpinionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Opinions.objects.all()
    serializer_class = OpinionSerializer
