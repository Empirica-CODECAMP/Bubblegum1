
from django.shortcuts import render
from .models import HealthIndexRawData

def health_index_view(request):
    data = HealthIndexRawData.objects.all()
    return render(request, 'data_table.html', {'data': data})
