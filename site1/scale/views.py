from django.shortcuts import render
from .models import weith as weight_model
from home.models import demoscale as scale_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Scaleserializer
from .models import weith

#from .models import 
# Create your views here.
def get_weight(request,id):
    weight_list = weight_model.objects.filter(scale_id = id)
    demoscale = scale_model.objects.get(scale_id =id)
    print(demoscale)
    return render(request,'weight.html',{'weight_list': weight_list ,'demoscale' : demoscale})

"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/scale-list/',
        'Detail View': '/scale-detail/<int:id>',
        'Create': '/scale-create/',
        

    }
    return Response(api_urls)
"""
@api_view(['GET'])
def ShowAll(request):
    w = weith.objects.all()
    serializer = Scaleserializer(w, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def Createdata(request):
    serializer = Scaleserializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
