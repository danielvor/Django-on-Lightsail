from django.shortcuts import render

# Create your views here.

def stopwatch(request):
    return render(request, 'stopwatch/stopwatch.html')