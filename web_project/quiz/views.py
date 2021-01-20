from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'quiz/index_template.html')

def pergunta(request):
    return render(request, 'quiz/pergunta_template.html')

def score(request):
    return render(request, 'quiz/score_template.html')