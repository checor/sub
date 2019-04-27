import json
from rest_framework.viewsets import ModelViewSet
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.views.generic import TemplateView
from .models import Linea, Estaciones
from .serializer import LineaSerializer, EstacionSerializer

# Create your views here.
class LineaView(ModelViewSet):
    queryset = Linea.objects.all().order_by('id')
    serializer_class = LineaSerializer

class EstacionView(ModelViewSet):
    queryset = Estaciones.objects.all().order_by('id')
    serializer_class = EstacionSerializer
    