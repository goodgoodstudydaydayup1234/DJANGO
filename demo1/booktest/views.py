from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookInfo, HeroInfo
from django.template import loader


def index(request):

    return render(request, 'booktest/index.html', {'username': 'xcy'})
    # temp = loader.get_template('booktest/index.html')
    # result = temp.render({'username': 'xcy'})
    # print(result, type(result))
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


def delete(request, id):
    # return HttpResponse('删除成功')
    BookInfo.objects.get(pk=id).delete()
    bl = BookInfo.objects.all()
    # return render(request, 'booktest/list.html', {'booklist': bl})
    return HttpResponseRedirect('/list/', {'booklist': bl})


def addhero(request, bookid):
    # return HttpResponse('角色添加成功')
    # books = BookInfo.objects.all()
    return render(request, 'booktest/addhero.html', {'bookid': bookid})


def addherohandle(request):
    bookid = request.POST['bookid']
    # bookid =5
    hname = request.POST["hname"]
    hgender = request.POST["hgender"]
    hcontent = request.POST["hcontent"]

    book = BookInfo.objects.get(pk=bookid)

    h = HeroInfo()
    h.hname = hname
    h.hgender = hgender
    h.hcontent = hcontent
    h.hbook = book

    h.save()

    return HttpResponseRedirect('/detail/'+str(bookid), {'book': book})

