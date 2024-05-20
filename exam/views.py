from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    que="who developed python?"
    a="Guido Van Rossum "
    b="Bell "

    #dictionary created 
    context={
        'que':que,
        'a':a,
        'options':[a,b],
    }

    template=loader.get_template('testpaper.html')
    res=template.render(context, request)    
    return HttpResponse(res)

def result(request):
    s="<h1>This is a test result</h1>"
    return HttpResponse(s)


#exam