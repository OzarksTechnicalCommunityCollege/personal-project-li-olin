from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader


# Create your views here.
from .models import Page

def articles(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def page_list(request):
    pages = Page.created.all()
    return render(
        request,
        'articles/page/list.html',
        {'pages': pages}
    )

def pageDetail(request, id):
    try:
        page = Page.created.get(id=id)
    except Page.DoesNotExist:
        raise Http404('Page not found')
    return render(
        request,
        'articles/page/detail.htm',
        {'page': page}
    )