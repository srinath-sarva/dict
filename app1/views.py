from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if (request.method=="POST"):
        n=request.POST['name']
        return HttpResponse(n)
    return render(request,"app1/index.html")


