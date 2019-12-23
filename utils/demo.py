from django.http import HttpResponse


def index(request):
    print('hahahah')
    return HttpResponse()


def demo(request):
    print('我是在lancer新增的demo视图')
    print('123')
    return HttpResponse()