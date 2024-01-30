from django.shortcuts import render
from .models import demoscale as scale_model 
# Create your views here.
def get_home(request):
    scale_list = scale_model.objects.filter().order_by('scale_id')
    return render(request,'home.html', {'scale_list' :scale_list})