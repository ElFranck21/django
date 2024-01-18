from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice


# Create your views here.
def index (request):
    question_list=Question.objects.order_by('-id')[:2]
    html= ''
    for question in question_list:
        html += f"<p>{question.id}-{question.question_text}</p>"
        context= {
            "question_list": question_list
        }
        return render(request, 'polls/index.html', context )

    return HttpResponse("<h1>Holaaaaa desde Django App</h1>")

def detail(request,question_id):
    question= get_object_or_404(Question,pk=question_id)
    context={"question": question}
    return render(request, 'polls/detail.html', context)

def vote(request,question_id):
    return HttpResponse("Contando votos de la pregunta %s" % question_id)

def results(request,question_id):
    return HttpResponse("Resultados de la pregunta %s" % question_id)


