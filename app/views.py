from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'shannu','L':[99,555,335,56]}
    return render(request,'looping.html',d)