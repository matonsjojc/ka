from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prva_stran(request):
    return render(request, 'ka/prva_stran.html')
