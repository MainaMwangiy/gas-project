from rest_framework import viewsets
from . import models
from . import serializers

class GasViewSet(viewsets.ModelViewSet):
    queryset = models.Gas.objects.all()
    serializer_class = serializers.GasSerializer
    
# create(), list(), retrieve(), destroy()