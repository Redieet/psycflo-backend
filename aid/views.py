from django.http import HttpResponse
from django.template import loader
from .models import AidRequest ,donors

def aid_objects(request):
    aids = AidRequest.objects.all()
    template = loader.get_template('Aidobjects.html')
    context = {
        'aids': aids,  
    }
    return HttpResponse(template.render(context, request))



'''def aid_objects(request):
    aids = AidRequest.objects.all()
    template = loader.get_template('Aidobjects.html')
    context = {
        'aids': aids,  
    }
    return HttpResponse(template.render(context, request))'''



from rest_framework import generics
from .serializers import AidRequestSerializer

class AidRequestCreateView(generics.CreateAPIView):
    queryset = AidRequest.objects.all()
    serializer_class = AidRequestSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class AidRequestListView(generics.ListAPIView):
    queryset = AidRequest.objects.all()
    serializer_class = AidRequestSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['fullname']  
    search_fields = ['fullname', 'email', 'country']

