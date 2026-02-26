from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import Page
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})


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