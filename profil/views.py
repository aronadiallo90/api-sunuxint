from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework import generics
from rest_framework.response import Response
 
from profil.models import Profil
from profil.serializers import ProfilSerializer
 
class ProfilAPIView(APIView):
    def get(self, *args, **kwargs):
        profil = Profil.objects.all()
        serializer = ProfilSerializer(profil, many=True)
        return Response(serializer.data)
    
class ProfilCreateview(generics.CreateAPIView):
        queryset = Profil.objects.all()
        serializer_class = ProfilSerializer

class ProfilUpdateview(generics.UpdateAPIView):
        queryset = Profil.objects.all()
        serializer_class = ProfilSerializer

class ProfilDeleteView(generics.DestroyAPIView):
        queryset = Profil.objects.all()
        serializer_class = ProfilSerializer