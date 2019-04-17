from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader


def index(request):

    return render(request, 'booktest/index.html', {'username': 'xcy'})
    # temp = loader.get_template('booktest/index.html')
    # result = temp.render({'username': 'xcy'})
    # return HttpResponse(result)


def list(request):
    bl = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {'booklist': bl})
    # temp = loader.get_template('booktest/list.html')
    # result = temp.render({'bname': '连城诀', 'pub_time': '2000年'})
    # return HttpResponse(result)


def detail(request, id):
    book = BookInfo.objects.get(pk=int(id))
    return render(request, 'booktest/detail.html', {'book': book})
    # try:
    #     return HttpResponse(BookInfo.objects.get(pk=int(id)))
    # # return HttpResponse('详情页'+str(id))
    # except:
    #     return HttpResponse('请输入正确的图书id')

