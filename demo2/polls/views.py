from django.shortcuts import render
from .models import Question,Choose
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def list(request):
    queslist = Question.objects.all()
    return render(request, 'polls/list.html', {'queslist': queslist})


def detail(request, quesid):
    ques = Question.objects.get(pk=quesid)
    return render(request, 'polls/detail.html', {'ques': ques})

def result(request):
    quesid = request.POST["quesid"]
    ques = Question.objects.get(pk=quesid)
    qvote = request.POST["vote"]
    choose = Choose.objects.get(pk=qvote)
    choose.cvote += 1
    choose.save()
    return render(request, 'polls/result.html', {'ques': ques})
