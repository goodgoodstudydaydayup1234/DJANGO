from django.shortcuts import render
from .models import Question,Choose
# Create your views here.


def list(request):
    queslist = Question.objects.all()
    return render(request, 'polls/list.html', {'queslist': queslist})


def detail(request, quesid):
    print(111111)
    ques = Question.objects.get(pk=quesid)
    # chooses = Question.choose_set.get()
    return render(request, 'polls/detail.html', {'ques': ques})

