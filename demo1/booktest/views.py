from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo


def index(request):
    return HttpResponse('首页')


def list(request):
    return HttpResponse('列表页')


def detail(request, id):
    try:
        return HttpResponse(BookInfo.objects.get(pk=int(id)))
    # return HttpResponse('详情页'+str(id))
    except:
        return HttpResponse('请输入正确的图书id')

