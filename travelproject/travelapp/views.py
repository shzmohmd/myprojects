from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
from . models import Argent

# Create your views here.

def demo(request):
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    ob = Argent.objects.all()

    return render(request, "index.html",{'result':obj, 'result2':obj2, 'resul':ob})


# def bas(request):
#     return render(request, 'basics.html')
#
#
# def abc(request):
#     return HttpResponse("Poda m@#$%^")
#
#
# def res(request):
#     val1 = int(request.GET['num1'])
#     val2 = int(request.GET['num2'])
#     add = val1 + val2
#     sub = val1 - val2
#     mul = val1 * val2
#     div = val1 / val2
#     return render(request, 'result.html', {'add': add, 'sub':sub,'mul':mul,'div':div})






