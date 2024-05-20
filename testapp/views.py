from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def greetings(request):
    s="<h1>Hello and welcome to first view</h1>"
    return HttpResponse(s)

def about(request):
    text="Future"
    template=loader.get_template('about.html')
    context={'text':text}
    res=template.render(context,request)
    return HttpResponse(res)


def contact(request):
    s="<h1>contact page</h1>"
    return HttpResponse(s)

# testapp
