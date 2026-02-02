from django.shortcuts import render
from django.http import Http404


# Create your views here.
from .models import Page
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