from django.shortcuts import render

# Create your views here.

def tictactoe(request):
    return render(request, 'tictactoe/tictactoe.html')